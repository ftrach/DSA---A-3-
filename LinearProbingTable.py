class LinearProbingTable:




    # ENTRY CLASS TO HOLD PAIRINGS OF IDENTIFIERS AND ASSOCIATED DATA



    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value





    # INITIALIZATION WITH DEFAULT SLOT COUNT





    def __init__(self, init_capacity=32):
        self.table_limit = init_capacity
        self.data_store = [None] * self.table_limit
        self.item_counter = 0





    # INTERNAL HASH FUNCTION BASED ON PYTHON'S BUILT-IN HASH





    def _compute_hash(self, key):
        return hash(key) % self.table_limit
    




    # LINEAR SCAN FOR A VACANT OR MATCHING SLOT




    def _linear_probe(self, initial_pos, key):
        probe_index = initial_pos
        while self.data_store[probe_index] is not None and self.data_store[probe_index].key != key:
            probe_index = (probe_index + 1) % self.table_limit
        return probe_index
    




    # ADD A NEW IDENTIFIER-DATA PAIR IF UNIQUE





    def insert(self, key, value):
        if self.item_counter / self.table_limit > 0.7:
            self._expand()

        probe_index = self._linear_probe(self._compute_hash(key), key)
        if self.data_store[probe_index] is not None:
            return False
        self.data_store[probe_index] = self.Record(key, value)
        self.item_counter += 1
        return True
    





    # UPDATE THE DATA FOR AN EXISTING IDENTIFIER





    def modify(self, key, value):
        probe_index = self._compute_hash(key)
        initial_probe = probe_index
        while self.data_store[probe_index] is not None:
            if self.data_store[probe_index].key == key:
                self.data_store[probe_index].value = value
                return True
            probe_index = (probe_index + 1) % self.table_limit
            if probe_index == initial_probe:
                break
        return False
    




    # DELETE AN IDENTIFIER-DATA ENTRY IF FOUND



    def remove(self, key):
        probe_index = self._compute_hash(key)
        initial_probe = probe_index
        while self.data_store[probe_index] is not None:
            if self.data_store[probe_index].key == key:
                self.data_store[probe_index] = None
                self.item_counter -= 1
                self._reinsert_all()
                return True
            probe_index = (probe_index + 1) % self.table_limit
            if probe_index == initial_probe:
                break
        return False
    





    # REINSERT ALL NON-EMPTY ENTRIES TO CLEAN GAPS






    def _reinsert_all(self):
        old_store = self.data_store
        self.data_store = [None] * self.table_limit
        self.item_counter = 0
        for node in old_store:
            if node:
                self.insert(node.key, node.value)






    # RETRIEVE DATA LINKED TO IDENTIFIER





    def search(self, key):
        probe_index = self._compute_hash(key)
        initial_probe = probe_index
        while self.data_store[probe_index] is not None:
            if self.data_store[probe_index].key == key:
                return self.data_store[probe_index].value
            probe_index = (probe_index + 1) % self.table_limit
            if probe_index == initial_probe:
                break
        return None





    # RETURN TOTAL SLOTS IN THE TABLE




    def capacity(self):
        return self.table_limit




    # RETURN NUMBER OF RECORDS CURRENTLY STORED




    def __len__(self):
        return self.item_counter





    # DOUBLE THE SIZE OF THE TABLE AND REHASH



    def _expand(self):
        old_store = self.data_store
        self.table_limit *= 2
        self.data_store = [None] * self.table_limit
        self.item_counter = 0
        for node in old_store:
            if node:
                self.insert(node.key, node.value)
