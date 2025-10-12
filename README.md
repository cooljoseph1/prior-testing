# How good are your priors?

I have run 1,000,000 experiments of 5 trials each. Every trial has a binary outcome, either L (for left) or R (for right).

However, I'm not going to tell you what my experiments are. Maybe I'm just flipping a fair coin each time. Maybe I'm using a biased coin. Or maybe I'm doing something completely different, like dropping a bouncy ball down a mountain and checking whether it hits a red rock or a white rock first.

Or maybe I'm doing some combination of the three. Nevertheless, you do have one guarantee: The trials in any one experiment are independent samples from the same Bernoulli distribution.

Your goal is to give me the marginal frequencies of the fifth trial's result, given the counts of Ls and Rs in the first four trials. Please give me a list of five frequencies of the fifth trial being an R, ordered from least Rs seen to most Rs seen. For example, your list might be [0.3, 0.4, 0.5, 0.6, 0.7]. Your list should probably be non-decreasing.

[Here is a csv of the public trials.](public.csv)

Note that I haven't yet actually calculated the frequencies myself, but I will do so shortly after posting this.
