# How good are your priors?

I have run 1,000,000 experiments of 5 trials each. Every trial has a binary outcome, either L (for left) or R (for right).

However, I'm not going to tell you what my experiments are. Maybe I'm just flipping a fair coin each time. Maybe I'm using a biased coin. Or maybe I'm doing something completely different, like dropping a bouncy ball down a mountain and checking whether it hits a red rock or a white rock first--and different experiments are conducted on different mountains. Or maybe I'm doing some combination of the three.

You do get one guarantee, though: All the experiments are Bernoulli processes. That is, the trials in each experiment are independent and have the same frequency of begin R as each other.

Your goal is to guess the marginal frequencies of the fifth trial, conditioned on the number of Rs seen in the first four trials. How this works is I create a bucket for each number of possible Rs seen in the first four trials: Either 0 Rs, 1 R, 2 Rs, 3 Rs, or 4 Rs. I then find, for each bucket, the fraction of experiments where the fifth trial is also an R.

For example, if every experiment is just flipping a fair coin, then the fifth trial will be an R with probability 1/2, no matter what the first four are. However, if I use a biased coin, then the frequency the fifth will be an R increases the more Rs you have already seen.

To help you in your guessing, I have provided a [csv of all the public trials](public.csv). As an answer, please provide a list like [0.3, 0.4, 0.5, 0.6, 0.7] of your frequencies of the fifth trial being an R given 0 Rs, 1 R, ..., 4 Rs in the first four trials.

Note that I haven't yet actually calculated the frequencies myself, but I will do so shortly after posting this.
