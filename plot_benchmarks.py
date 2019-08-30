import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


for infile in ["benchmarks_including_copy.txt", "benchmarks_without_copy.txt"]:
    b = pd.read_csv(infile, sep=' ')
    b['seconds_snp'] = b.seconds/b.nmutations
    print(b.seconds_snp.min())
    # p = sns.scatterplot(x='nsam', y='seconds_snp',
    p = sns.scatterplot(x='nsam', y='seconds',
                        hue='toolkit', style='Nu',
                        data=b, alpha= 0.5)
    plot = p.get_figure()
    #plt.ylim(0.0, 0.0006)
    plt.xscale('log')
    #plt.legend(loc=2,bbox_to_anchor=(1,1))
    of = infile.replace("txt","png")
    plot.savefig(of, dpi=300)
