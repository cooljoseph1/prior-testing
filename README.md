# How good are your priors?

I have run 1,000,000 experiments of 5 trials each. Every trial has a binary outcome, either $L$ (for left) or $R$ (for right).

However, I'm not going to tell you how I've picked my experiments. Maybe I'm just flipping a fair coin each time. Maybe I'm using a biased coin. Or maybe I'm doing something completely different, like dropping a bouncy ball down a mountain and checking whether it hits a red rock or a white rock first--and different experiments are conducted on different mountains. Or maybe I'm doing some combination of all three.

You do get one guarantee, though: All the experiments are Bernoulli processes. In particular, the *order* of the trials is irrelevant.

Your goal is to guess the marginal frequencies of the fifth trial. For each $k = 0, 1, \dots, 4$, you need to tell me the frequency that the fifth trial is an $R$ given that $k$ of the outcomes of the first four trials are $R$.

For example, if every experiment is just flipping a fair coin, then the fifth trial will be an $R$ with probability $1/2$, no matter what the first four are. However, if I'm using biased coins, then the frequency of $R$ will increase the more $R$s seen.

To help you in your guessing, I have provided a [csv of all the public trials](public.csv). As an answer, please provide a list like [0.3, 0.4, 0.5, 0.6, 0.7] of your frequencies--the kth element of your list is the marginal frequency over the experiments with $k$ of the first four trials being $R$.

I haven't yet actually calculated the frequencies myself, but I will do so shortly after posting this.
