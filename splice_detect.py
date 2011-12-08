#!/usr/bin/python


def splice_detect(base="", recalc = True):

    # (re-)calculate model parameters and scores
    #
    if recalc:
        # model parameters -- based on training data
        #
        from Quotients import Quotients
        Quotients('markov_pos.json').makeJson(open(base+'train_pos.txt', 'r'))
        Quotients('markov_neg.json').makeJson(open(base+'train_neg.txt', 'r'))

        # scores -- based on test data
        #
        import scorecalc
        orig_out = sys.stdout
        sys.stdout = open('scores_pos.json', 'w')
        scorecalc.main('markov_pos.json', 'markov_neg.json', base+'test_pos.txt')
        sys.stdout = open('scores_neg.json', 'w')
        scorecalc.main('markov_pos.json', 'markov_neg.json', base+'test_neg.txt')
        sys.stdout = orig_out

    # create a plot object and plot the score histograms in a background thread
    #
    from plotMarkov import PlotMarkov
    from threading import Thread
    pm = PlotMarkov('scores_pos.json', 'scores_neg.json')
    Thread(target = pm.plot).start()

    # decide on the optimal cut-off value
    #
    import decide
    decide.decide()

if __name__ == "__main__":

    base = ""
    recalc = True

    import sys
    for arg in sys.argv[1:]:
        if arg == "-nr":
            recalc = False
        elif arg[0] == "-":
            print "usage: %s [-nr] [data directory]" % sys.argv[0]
            print "  -nr: don't recalculate the scores"
            sys.exit(1)
        else:
            import os
            base = arg.rstrip(os.sep) + os.sep

    try:
        splice_detect(base=base, recalc=recalc)
    except IOError, e:
        from errno import errorcode
        if errorcode[e.errno] == 'ENOENT':
            print "ERROR: data files not found!"
            print
            print "either change the current directory,"
            print "or     copy / link the data files into the current directory,"
            print "or     supply the data directory as a command-line argument to this script."
            print
            print "alternatively, you can use the -nr option,"
            print " if you don't want to recalculate the scores anyway --> no data files needed"

