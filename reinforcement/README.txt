I. Question 1 (6 points): Value Iteration

computeQValueFromValues calculate the value for certain (state, action) for mdp.

In the init, by using computeQValueFromValues to calculting best action QValue, run iterations times for updating every state.

In the computeActionFromValue, just try all actions and choose one that gives the best value. It call computeQValueFromValues for calculating certain value.

The reason why in init, I did not use computeActionFromValues is that it saves one loop by directly compute best value instead of firtly compute best action and generate best value for that best action.

II. Question 2 (1 point): Bridge Crossing Analysis

Simply change noise to 0.0, then the chasms are actually ignored in calculation because when the noise is 0.0 there's no opportunity for the agent to get to any chasm.

III. Question 3 (5 points): Policies

a. Make noise to 0.0 to risk cliff, add discount and negative living reward to make it worthier to get to the closer exit.

b. High noise makes the agent avoid the cliff, tune discount and living reward to make it worthier to get to the closer exit.

c. Make noise to 0.0 to risk cliff, high discount value to make it worthier to get to distant exit.

d. High discount value to make it worthier to get to distant exit, keep certain value of noise to avoid the cliff.

e. Positive living reward make agent don't want to exit, discount should be 1.0 if the iteration is large enough to prevent convergence.

IV. Question 4 (5 points): Q-Learning

In init, create a member varaible name values of type util.Counter to save QValues.

getQValue simply return value from self.values with key (state, action)

computeActionFromQValues simply returns the action that returns the best QValue for certain state.

computeValueFromQValues returns the best QValue of a state by calling getQValue with state, and best action for that state.

V. Question 5 (3 points): Epsilon Greedy

Simply use util.flipCoin to decide whether choose actions randomly or choose the best.

VI. Question 6 (1 point): Bridge Crossing Revisited

It's not possible, can be proved easily by a thought experiment and inference.

Firstly, before the agent has reached +10 exit, the QValue for east will never effected by +10 exit, and apprently compare to west QValue, west will be bigger than east all the time. For north and south, because of the cliff, it's either zero or negative.

Consider the best situation. East will never be the unique best action, the possibility to go east for a single move must be less than 1/2. 1/2, that's the best possibility. So for a iteration, the agent must go at least 5 steps east to reach the +10 exit. The possibility is

P(reached +10 for 1 iteration) < (1 / 2)^5 = 1 / 32

Because after 1 iteration, the possibility to go east still will never pass 1 / 2, so every iteration is actually independent in this best situation thought experiment.

P(reached +10 during 50 iterations) < 1 - (31/32)^50 = 79.56 %

79.56 % is much lower than 99%, and it's just the possibility for the agent to reach +10 exit for at least once in 50 iteration! (reach +10 once is not enough to find the optimal path) And it's a value calculated in the best situation hypothesis!

That's it, it's actually highly impossible to reach find an optimal path rather than highly possible.


VII. Question 7 (1 point): Q-Learning and Pacman

I did not alter any code and question 7 works fine and autograder passed.

VIII. Question 8 (3 points): Approximate Q-Learning

getQValue returns the result of multiple of two vectors, one is weights, one is features. It just like calculating a linear formula.

update updates the value according to the given formula. problem is that weights and features are vectors, it's more intuitive to utilize vector operations. Since the multiplication of all elements by a multiplier in a vector did not implemented in util.Counter, so I have to add mulAll function by myself.

