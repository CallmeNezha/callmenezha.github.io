Title: A word to my future self.
Date: 2023-03-13 10:40
Category: Words
Tags: Words

# 2023-03-13 10:40
Learn by doing, hands-on first.

# 2023-03-13 11:02
I'm cloning the vscode git repo to study it's debugging features, git's storage costs 1.2G bytes! What a huge repository this is!

# 2023-03-18 15:29
VScode uses interface classes extensively, you can see advanced Inverse of Control everywhere. It seems that VScode has indeed learned a lot from Eclipse's years of IDE development. Designing rigorous interfaces using Inverse of Control allows for the precise definition of highly controlled yet general processes. It can only be done after solving numerous problems with similar pattern, and summing up the essence. The mastermind behind both VSCode and Eclipse is Erich Gamma.

# 2023-03-18 16:00
Looking at the entry of an api object reminds me of level of detail. Abstracting the level of detail well, then you will get clean code natually.

# 2023-03-18 22:22
At its core, the design of software architecture is about isolation and classification. So where to put the responsibility(api of class, objects and modules) matters.

# 2023-03-19 21:16
I finally realized that VScode use an 'factory 'interface class that only contains one method, because VScode main designer comes from technical background in Eclipse(Java), so they are still not get used to treating functions as first-class memebers of programming languages. So I don't think it's necessary to have `XXfactory` classes which implement only one `createXX` method, I can just use function which named `XXprovider` or `XXforger` instead, it's much simpler.

# 2023-03-20 21:41
Why do I like to use Pycharm/VScode to develop software, but use Jupyter to analyze and transform data? 