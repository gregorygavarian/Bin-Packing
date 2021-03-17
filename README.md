# Bin-Packing

The bin packing problem is conceptually simple.  You have bins of a given size, and numerous smaller objects which can fit into them.  The problem asks, how can one arrange the items into the bins so as to minimize the number of bins.  I originally began researching this problem a few months back, after recalling a friend say that NY state was considering putting a fee on each package delivery in order to recoup some of the debt incurred during COVID.  It would therefore be optimal to be able to order everything on my wish list while using as few packages as possible.

This could of course be accomplished by simply buying _everything_ on the wishlist in a single purchase order, but I want to constrain it to say, $30 per order.

Before I start, I will say that there are heuristic algorithms for solving this already.  They will give good answers that are probably close to the optimal solution, but are not guaranteed to be the optimal solution.  Being an NP-hard problem, it is uncertain if there _even is_ an algorithm for the optimal solution.  This is a brute-force algorithm.  It is not a very efficient approach, I _know_ it's not a very efficient approach, but it's provided here nonetheless.

In a generic view, for n items, the minimum number of possible bins is one, with a maximum number of n bins, with one item per bin.  

For two items, A and B, they can be categorized as follows, with each numerical pair corresponding to which bin that item A or B corresponds to:

AB
11
12
21
22

For three items, A, B, and C, they can be categorized as follows:
ABC
111
112
113
121
122
123
131
132
133
211
212
213
221
222
223
231
232
233
311
312
313
321
322
323
331
332
333

If we try this with 4 items, we'd get 256 possibilities.  This is a n^n relationship.  The number of bin possibilities is the number of items to the power of itself.

This function blows up _quickly_.  Two items means four possible arrangements.  Four items means 256.  Five means 3,125.  Ten means ten billion.  Twenty items would mean enough possible arrangements as there are atoms in the human body.  Forty items means as many possible arrangements as there are grains of sand that could fit into a sphere with a diameter of two light years.  Needless to say, this algorithm will be kept to small numbers of items.
