# associationRules_AprioriAlgorithm

In this project, I experimented with finding frequent itemsets and association rules, calculating support, confidence, and lift to evaluate association rules in song lyrics. I made use of the apriori algorithm on the collected dataset of songs. 

Some example rules from the song list of Soft Pop Genre:

One rule, with support 0.37, is the itemset ['you', 'me', 'love']
 ['me', 'love'] --> ['you'] confidence: 1.00 lift: 1.50
 
 ['you', 'love'] --> ['me'] confidence: 1.00 lift: 1.96
 
 ['me', 'you'] --> ['love'] confidence: 0.77 lift: 2.05
 
This one is interesting- highest confidence for the pairings that make sense: me love -> you and, you love -> me. The confidence is lower for me you -> love. This grammatically makes sense. Also interesting note, while confidence is high for the first two association rules, the "you love -> me" has a slightly higher support, maybe indicating that this phrase occurs less often the "me love -> you". Maybe because this artist is conveying they love someone else, not someone else loves them, more. 



Another rule, with support 0.34, is the itemset ['you']
 [] --> ['you'] confidence: 0.35 lift: 1.00
 
Rule with support 0.32, and itemset ['on', 'holding']

 ['holding'] --> ['on'] confidence: 1.00 lift: 3.07
 
 ['on'] --> ['holding'] confidence: 1.00 lift: 3.07
 
This song also references the term "you" and talks about "holding on"- again, showing a high interest in someone else and holding on to something (possibly that person or some feeling)


 
Rule with support 0.33 with itemset ['ι', 'would', 'never', 'thought']

 ['would', 'never', 'thought'] --> ['ι'] confidence: 1.00 lift: 1.73
 
 ['ι', 'never', 'thought'] --> ['would'] confidence: 0.71 lift: 1.89
 
 ['ι', 'would', 'never'] --> ['thought'] confidence: 1.00 lift: 2.14
 
 ['ι', 'would', 'thought'] --> ['never'] confidence: 1.00 lift: 1.96
 
This rule also indicates that this genre has association rules possibly related to emotions, thinking and feelings, indicated by the phrases "i, would and thought" in the same itemset.


It seems to me that Country genre shows lyrics that is much more self-interested and surface level. For example, [me], [you,like]->[me],[i] and [she], seem to be the most important items with no items indicating much about thinking. Soft Pop rather seemed to be more focused on emotions and feelings, particularly related to someone else ([you,love]).
