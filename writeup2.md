# Results of "Experiment on Bernoulli processes"

Two weeks ago I posted [an experiment for priors on Bernoulli processes](https://www.lesswrong.com/posts/mgSxBpYvAYPJf2uYb/experiment-test-your-priors-on-bernoulli-processes). I gave you all way too much data, though, so I don't think it worked out to be a very good experiment.

This post provides the correct results and explains what the hidden experiments were.

## Motivation Behind the Experiment

I was thinking about induction. Suppose you are a Bayesian, and you only have a small number of observations about some time-invariant law. What is the *correct* posterior you should have after these observations? If you just go with the bare observed frequencies, then you will be hopelessly overconfident if you see only a string of yesses or nos.

Your posterior follows directly from your prior, so this is equivalently a question on what the correct *prior* is. Some people have proposed Jeffreys priors or Laplace's rule of succession as non-informative priors. But do these priors actually lead to correct posteriors?

I wanted to put that to the test, experimentally. Naturally, a large part of the test would be how well you could predict *me*. But that doesn't make it a worthless test. Unfortunately, I gave you guys way too much data, and so it didn't really matter what prior you used. I think the experiment would have been much more interesting if I only provided 100 experiments, and then computed the true marginals on a held-out dataset.

## Results

The correct answers were $11.01\%, 32.49\%, 50.00\%, 67.41\%,$ and $88.95\%$. Here's a table of the total number of experiments for each count of $R$s in the first four trials:

| $R$s in First Four Trials | # Experiments | # Final Trial is $R$ | Marginal Frequency |
|-------------|---------------|--------------|---------------|
| 0           | 253,099       | 27,856       | 11.01%         |
| 1           | 166,571       | 54,125       | 32.49%         |
| 2           | 161,832       | 80,924       | 50.00%         |
| 3           | 165,890       | 111,825      | 67.41%         |
| 4           | 252,608       | 224,700      | 88.95%         |

Now that the challenge is over, I've posted [all of the data online](https://github.com/cooljoseph1/prior-testing/raw/refs/heads/main/all_data.csv).

Most of you were very close, only off by a few parts in 10,000. I was
especially impressed by Cleo Nardo's submission. She guessed 10.6%, 34.8%, 50%, 65.2%, and 89.4% without even looking at the CSV, which were all within a couple percent of the correct values.


## The Bernoulli Processes

There were four types of experiments.
1. **A fair coin**. In this experiment, each trial had a 50% chance exactly of giving $R$.
2. **A slider coin**. In this experiment, a coin bias $p$ was chosen from $[0, 1]$ uniformly at random, and then each trial had a $p$ chance of giving $R$.
3. **A filtered slider coin**. Like in case (2), a coin bias $p$ was chosen uniformly from $[0, 1]$. Unlike in case (2), the coin was only accepted if its first three flips were $R$ (half the time) or $L$ (the other half of the time). Coins would keep being selected until one passed the filter, and then that would be the coin for the experiment.
4. **A frog hop**. A frog is placed on the middle lily pad of a line of seven lily pads. Every minute, it hops left or right. Eventually, it will hop off the line of lily pads to the right or the left. Each trial's result is which side it hops off. An experiment is constructed by choosing fixed hop probabilities for each lily pad independently and uniformly from $[0, 1]$.

The four types of experiments were mixed with weights 10%, 10%, 10%, and 70%.

The second and third cases can both be viewed as drawing the Bernoulli probability from a mixture of Beta distributions (so that the correct prior is a Beta prior). For case (2), the Beta distribution is $\mathrm{Beta}(1, 1)$, and for case (3), the distribution is an even mixture of $\mathrm{Beta}(1, 4)$ and $\mathrm{Beta}(4, 1)$.

Cases (1) and (4) do not have Beta priors. Case (4) in particular is tricky. The probability for the Bernoulli process is the stationary point of a Markov chain, which involves multiplying and adding many random variables together.

## Calculating the True Marginal Probabilities

The marginals in the first three cases can be calculated analytically very easily. I think the fourth case can also be analytically solved, but I chose to use a Monte Carlo simulation instead. To get better accuracy, I used two tricks:
1. Instead of actually running the trials for each experiment, I calculated the stationary point of the Markov chain to get the Bernoulli probability $p$, which allowed me to compute the exact marginal probabilities (and their weights) for that experiment.
2. I used PyTorch and the GPU to parallelize 10 billion experiments.

Combining everything together, I got the true marginal probabilities to six significant figures (so 5 accurate digits). They are $11.0810\%, 32.5015\%, 49.9997\%, 67.4990\%,$ and $88.9188\%$.

## Who wins?

Because you all were so close, I decided to resort to the true probabilities to determine a winner. My scoring function is the KL divergence from the true marginal probability to your guess, for each of the five marginal probabilities. Your scores for your public submissions are
| Name            | Score        |
|-----------------|--------------|
| Unnamed         | 0.0000015762 |
| One             | 0.0000015850 |
| DaemonicSigil   | 0.0000029092 |
| James Camacho   | 0.0016014697 |
| Cleo Nardo      | 0.0025952372 |

This means that Unnamed wins. Congratulations!

## Resolving the Manifold Market
As promised, I resolved the Manifold market using the marginals for the original 1,000,000 trials. Manifold Markets didn't allow me to resolve to a sub-percentage precision, so I randomly rounded a percentage $x$ to its ceiling or floor with probabilities $\{x\}$ and $1 - \{x\}$, where $\{x\}$ is the fractional part of $x$.
