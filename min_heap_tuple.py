class BinaryHeap:
    """A min-heap implementation for tuples with first value as integer.
    
    The heap maintains the min-heap property: each parent node is less than
    or equal to its children. This allows efficient O(log n) insertion and
    extraction of the minimum element.
    """
    
    def __init__(self):
        """Initialize an empty binary heap."""
        self.data = []

    def insert(self, value: tuple) -> None:
        """Insert a value into the heap.
        
        Args:
            value: The integer value to insert.
        """
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def extract_min(self) -> tuple:
        """Remove and return the minimum element from the heap.
        
        Returns:
            The smallest element in the heap or None if empty.
        """
        if not self.data:
            return None
        
        min_val = self.data[0]
        last = self.data.pop()
        
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        
        return min_val

    def delete(self, value: tuple) -> bool:
        """Delete a value from the heap.
        
        Args:
            value: The tuple value to delete.
            
        Returns:
            True if the value was found and deleted, False otherwise.
        """
        try:
            index = self.data.index(value)
        except ValueError:
            return False
        
        last = self.data.pop()
        
        if index < len(self.data):
            self.data[index] = last
            if self.data[index] < self.data[self._get_parent(index)]:
                self._sift_up(index)
            else:
                self._sift_down(index)
        
        return True
    
    def contains(self, value: tuple) -> bool:
        """Check if a value exists in the heap.
        
        Args:
            value: The integer value to search for.
            
        Returns:
            True if the value exists in the heap, False otherwise.
        """
        for candidate_value in self.data:
            if candidate_value == value: 
                return True
        return False


    def heapify(data: list[int]) -> 'BinaryHeap':
        """Build a BinaryHeap from an unordered list using Floyd's algorithm.
    
        This constructs the heap in O(n) time by starting from the last parent
        node and sifting down each subtree. This is more efficient than inserting
        elements one by one (O(n log n)).
        
        Args:
            data: A list of integers to convert into a min-heap.
            
        Returns:
            A BinaryHeap containing the elements from the input list.
        """
        heap = BinaryHeap()
        heap.data = data.copy()
        
        size = len(data)
        last_parent = (size - 1) // 2
        
        for i in range(last_parent, -1, -1):
            heap._sift_down(i)
        
        return heap

    def _swap(self, i: int, j: int) -> None:
        """Swap two elements in the heap.
        
        Args:
            i: Index of the first element.
            j: Index of the second element.
        """
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _sift_up(self, index: int) -> None:
        """Move an element up the heap to restore the min-heap property.
        
        Starting from the given index, repeatedly swap the element with its
        parent if it is smaller. This is used after insertions.
        
        Args:
            index: The index of the element to sift up.
        """
        while index > 0:
            parent = self._get_parent(index)
            if self.data[index][0] < self.data[parent][0]:
                self._swap(index, parent)
                index = parent
            else:
                break
        return

    def _get_children(self, parent_index: int) -> tuple[int, int]:
        """Get the child indices for a given parent index.
        
        Args:
            parent_index: The index of the parent node.
            
        Returns:
            A tuple of (left_child_index, right_child_index).
        """
        left = 2 * parent_index + 1
        right = 2 * parent_index + 2
        return left, right
    
    def _get_parent(self, index: int) -> int:
        """Get the parent index for a given index.
        
        Args:
            index: The index of the child node.
            
        Returns:
            The index of the parent node.
        """
        return (index - 1) // 2

    def _sift_down(self, index: int) -> None:
        """Move an element down the heap to restore the min-heap property.
        
        Starting from the given index, repeatedly swap the element with the
        smaller of its two children if it is larger. This is used after
        extraction or deletion.
        
        Args:
            index: The index of the element to sift down.
        """
        while True:
            left, right = self._get_children(index)
            smallest = index
            
            if left < len(self.data) and self.data[left][0] < self.data[smallest][0]:
                smallest = left
            if right < len(self.data) and self.data[right][0] < self.data[smallest][0]:
                smallest = right
            
            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def __str__(self):
        return str(self.data)