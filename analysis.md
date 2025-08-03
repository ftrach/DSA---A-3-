


# PART A: SORTED  TABLE FUNCTION ANALYSIS









### FUNCTION: insert(self, key, value)


  -   TIME COMPLEXITY: O(n^2)  


  -   REASON: linear scan to check for duplicate keys followed by bubble sort after adding the new element  .  


  -   INEFFICIENCY: bubble sort is inefficient for larger datasets


  -   SUGGESTION: consider binary search and insertion at the correct index to maintain sort order without full sort









### FUNCTION: modify(self, key, value)


  -   TIME COMPLEXITY: O(n)  


  -   REASON: linear search is used to find the key


  -   INEFFICIENCY: unnecessary linear traversal in a sorted structure


  -   SUGGESTION: using binary search would reduce lookup time significantly










### FUNCTION: remove(self, key)


  -   TIME COMPLEXITY: O(n)  


  -   REASON: linear scan to locate the key, followed by shifting all elements left


  -   INEFFICIENCY: shifting elements is computationally expensive for large tables


  -   SUGGESTION: use binary search to locate the index, and consider linked list to avoid shifting











### FUNCTION: search(self, key)


- TIME COMPLEXITY: O(n) 


- REASON: a sequential search is used to locate the key


- INEFFICIENCY: poor use of sorted structure for fast lookups


- SUGGESTION: switch to binary search to take advantage of sorted nature












### FUNCTION: capacity(self)


- TIME COMPLEXITY: O(1)  


- REASON: directly returns the table's capacity attribute


- INEFFICIENCY: none


- SUGGESTION: no changes needed










### FUNCTION: __len__(self)


- TIME COMPLEXITY: O(n)  


- REASON: counts how many entries in the table are not None


- INEFFICIENCY: repeated scanning of the entire list each time length is requested


- SUGGESTION: maintain a separate size counter for real-time length updates

