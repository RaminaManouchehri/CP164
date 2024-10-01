"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-28"
-------------------------------------------------------
"""
from copy import deepcopy


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        if self._front is None:
            node = _List_Node(value, None)
            self._front = node
            self._rear = node
        else:
            node = _List_Node(value, self._front)
            self._front = node
        self._count += 1
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        node = _List_Node(value, None)
        if self._front is None:
            self._front = node
            self._rear = self._front
        else:
            self._rear._next = node
            self._rear = node
        self._rear._next = None
        self._count += 1
        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        if i == 0 or i < self._count * -1:
            self.prepend(value)
        elif i >= self._count:
            self.append(value)
        else:
            current = self._front
            if i < 0:
                i = self._count + i
            while i > 1:
                current = current._next
                i -= 1
            current._next = _List_Node(value, current._next)
            self._count += 1
        
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """
        # your code here
        previous = None
        current = self._front
        index = 0

        while current is not None and current._value != key:
            # print(current._value, end=", ")
            previous = current
            current = current._next
            index += 1

        if current is None:
            index = -1
        return previous, current, index
    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        if pln is not prn:
            # Swap only if two nodes are not the same node

            if pln is None:
                # Make r the new front
                left = self._front
                self._front = prn._next
            else:
                left = pln._next
                pln._next = prn._next

            if prn is None:
                # Make l the new front
                right = self._front
                self._front = left
            else:
                right = prn._next
                prn._next = left

            # Swap next pointers
            # lst._next, r._next = r._next, lst._next
            temp = left._next
            left._next = right._next
            right._next = temp
            # Update the rear
            if right._next is None:
                self._rear = right
            elif left._next is None:
                self._rear = left
        return
    def _append_list(self, source):
        """
        -------------------------------------------------------
        Private helper method to append the entire source List to the
        rear of the target List.
        Either the source List or the target List may be empty.
        The source list becomes empty.
        Use: target.append_list(source)
        -------------------------------------------------------
        Parameters:
            source - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        if source._front is not None:
            # If source is empty, target (self) is unchanged.
            # Update the target List.
            if self._rear is None:
                # Current queue is empty.
                self._front = source._front
            else:
                self._rear._next = source._front
            self._rear = source._rear
            self._count += source._count
            # Empty the source list.
            source._front = None
            source._rear = None
            source._count = 0
        return
    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # your code here
        value = None
        previous, current, index = self._linear_search(key)
        if index != -1:
            if self._count == 1:
                value = self._front._value
                self._front = None
                self._rear = None
            elif index == 0:
                value = self._front._value
                self._front = self._front._next
            elif index == (self._count - 1):
                value = self._rear._value
                self._rear = previous
                previous._next = None
            else:
                value = current._value
                previous._next = current._next
            self._count -= 1
        
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        # your code here
        value = self._front._value
        if self._count == 1:
            self._front = None
            self._rear = None
        else:
            self._front = self._front._next
        self._count -= 1
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        previous, current, index = self._linear_search(key)
        while index != -1:
            if self._count == 1:
                self._front = None
                self._rear = None
            elif self._count != 1 and index == 0:
                self._front = self._front._next
            elif index == (self._count - 1):
                self._rear = previous
                previous._next = None
            else:
                previous._next = current._next
            self._count -= 1
            previous, current, index = self._linear_search(key)
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # your code here
        previous, current, index = self._linear_search(key)
        if index != -1:
            value = current._value
        else:
            value = None
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        # your code here
        return deepcopy(self._front._value)

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        # your code here
        previous, current, index = self._linear_search(key)
        return index

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        # your code here
        current = self._front
        index = 0
        if i < 0:
            i = self._count + i
        if i == 0:
            current = self._front
        else:
            while index < i:
                current = current._next
                index += 1
        value = current._value
        return value

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        # your code here
        current = self._front
        index = 0
        if i < 0:
            i = self._count + i
        if i == 0:
            self._front._value = deepcopy(value)
        else:
            while index < i:
                current = current._next
                index += 1
            current._value = deepcopy(value)
        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        previous, current, index = self._linear_search(key)
        
        return index != -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        # your code here
        max_data = self._front._value
        i = 0
        current = self._front
        while i < self._count:
            if current._value > max_data:
                max_data = current._value
            current = current._next
            i +=1
            
        return max_data

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        # your code here
        min_data = self._front._value
        i = 0
        current = self._front
        while i < self._count:
            if current._value < min_data:
                min_data = current._value
            current = current._next
            i +=1
        return min_data

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        # your code here
        current = self._front
        i = 0
        number = 0
        while i < self._count:
            if current._value == key:
                number += 1
            current = current._next
            i +=1
        return number

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        # your code here
        self._rear = self._front
        previous = None
        current = self._front
    
        while current is not None:
            temp = current._next
            current._next = previous
            previous = current
            current = temp
    
        self._front = previous
        return

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        # your code here
        if self._count > 1:
            self._rear = self._front
            self.reverse_r_aux(None, self._front)
        return
    def reverse_r_aux(self, previous, current):
        if current is None:
            self._front = previous
        else:
            temp = current._next
            current._next = previous
            self.reverse_r_aux(current, temp)
        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        llist = List()
        previous = None
        current = self._front

        while current is not None:
            if current._value not in llist:
                llist.append(current._value)
                previous = current
            else:
                self._count -= 1
                if current == self._rear:
                    previous._next = None
                    self._rear = previous
                else:
                    previous._next = current._next
                if self._count == 0:
                    self._rear = None
                    self._front = None
            current = current._next
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value


    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a list (List)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        i = 0
        scurrent = self._front
        tcurrent = target._front
        equals = True
        if self._count == target._count:
            while equals and i < self._count:
                if scurrent._value != tcurrent._value:
                    equals = False
                scurrent = scurrent._next
                tcurrent = tcurrent._next
                i +=1
        else:
            equals = False
        return equals
    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values as
                target in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != target._count:
            identical = False
        else:
            source_node = self._front
            target_node = target._front
    
            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next
    
            identical = source_node is None
        return identical

    def is_identical_r(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = source.is_identical_r(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        # your code here
        if self._count != target._count:
            identical = False
        else:
            identical = self.is_identical_r_aux(self._front, target._front)
        return identical
    def is_identical_r_aux(self, scurrent, tcurrent):
        identical = False
        if scurrent is None:
            identical = True
        else:
            if scurrent._value == tcurrent._value:
                identical = self.is_identical_r_aux(scurrent._next, tcurrent._next)
        return identical

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        # your code here
        target1 = List()
        target2 = List()
        if self._count % 2 != 0:
            count1 = (self._count // 2) + 1
            count2 = (self._count // 2) 
        else:
            count1 = (self._count // 2) 
            count2 = (self._count // 2) 
        i = 0
        j = 0
        while i < count1:
            target1._move_front_to_rear(self)
            i +=1
        while j < count2:
            target2._move_front_to_rear(self)
            j +=1
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source self is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        # your code here
        target1 = List()
        target2 = List()
        left = True
        while self._front is not None:
            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left
        return target1, target2

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty.
        Order of even and odd is not significant.
        (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
        # your code here
        even = List()
        odd = List()
        even, odd = self.split_alt_r_aux(odd, even)
        return even, odd
    def split_alt_r_aux(self, odd, even):
        if self._front is not None:
            even._move_front_to_rear(self)
            if self._front is not None:
                odd._move_front_to_rear(self)
            self.split_alt_r_aux(odd, even)
        return even, odd

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search_r(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        # your code here
        previous, current, index = self._linear_search_r_aux(key, None, self._front, 0)
        if current is None:
            index = -1
        return previous, current, index
    def _linear_search_r_aux(self, key, previous, current, index):
        if current is None:
            index = -1
        elif current._value != key:
            previous, current, index = self._linear_search_r_aux(key, current, current._next, index + 1)
        return previous, current, index

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        i = 0
        if source1._front is not None:
            node = source1._front
            while i < source1._count:
                previous, current, index = source2._linear_search(node._value)
                if index != -1:
                    previous, current, index = self._linear_search(node._value)
                    if index == -1:
                        self.append(node._value)
                node = node._next
                i +=1
        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        self.intersection_r_aux(source1._front, source2)
        return
    def intersection_r_aux(self, source1_node, source2):
        if source1_node is not None:
            previous, current, index = source2._linear_search_r(source1_node._value)
            if index != -1:
                previous, current, index = self._linear_search_r(source1_node._value)
                if index == -1:
                    self.append(source1_node._value)
            self.intersection_r_aux(source1_node._next, source2)
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        i = 0
        current1 = source1._front
        current2 = source2._front
        while i < source1._count:
            if current1 is not None:
                previous, current, index = self._linear_search(current1._value)
                if index == -1:
                    self.append(current1._value)
                if current1._next is not None:
                    current1 = current1._next
            i +=1
        i = 0
        while i < source2._count:
            if current2 is not None:
                previous, current, index = self._linear_search(current2._value)
                if index == -1:
                    self.append(current2._value)
                if current2._next is not None:
                    current2 = current2._next
            i +=1
        
        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        source1_node = source1._front
        source2_node = source2._front
        if source1_node is not None:
            self._union_r_aux( source1_node)
        if source2_node is not None:
            self._union_r_aux( source2_node)
        return

    def _union_r_aux(self,  source_node):
        if source_node is not None:      
            value = source_node._value
            _, current, _ = self._linear_search(value)
            if current is None:
                self.append(value)
            self._union_r_aux( source_node._next)
        return
    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        # your code here
        self._clean_r_aux(self._front, None, 0)
        return
    def _clean_r_aux(self, node, previous, index):
        temp = []
        if node is not None:
            if node._value not in temp:
                temp.append(node._value)
            else:
                if index == (self._count - 1):
                    previous._next = None
                    node = None
                else:
                    previous._next = node._next
                self._count -=1
            self._clean_r_aux(node._next, node, index + 1)
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish, self
        is empty.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        # your code here
        target1 = List()
        target2 = List()
        while self._front is not None:
            if self._front._value < key:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
        return target1, target2

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        # your code here
        new_list = List()
        current = self._front
        while current is not None:
            new_list.append(current._value)
            current = current._next
        return new_list

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        # your code here
        new_list = List()
        new_list = self._copy_r_aux(self._front, new_list)
        return new_list
    def _copy_r_aux(self, current, new_list):
        if current is not None:
            new_list.append(current._value)
            self._copy_r_aux(current._next, new_list)
        return new_list

    def reverse_pc(self):
        """
        -------------------------------------------------------
        Reverses a list through partitioning and concatenation.
        Use: lst.reverse_pc()
        -------------------------------------------------------
        Returns:
            The contents of the current list are reversed.
        -------------------------------------------------------
        """
        # your code here
        return

    def _move_front_to_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the front
        of the current List. Private helper method.
        Use: self._move_front_to_front(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        # your code here
        if self._front is None:
            self._front = source._front
            self._rear = self._front
        else:
            self._front = source._front
        self._count += 1
        if source._count == 1:
            source._front = None
            source._rear = None
        else:
            source._front = source._front._next
        source._count -=1
        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        # your code here
        if self._front is None:
            self._front = source._front
            self._rear = self._front
        else:
            self._rear._next = source._front
            self._rear = source._front
        self._count += 1
        if source._count == 1:
            source._front = None
            source._rear = None
        else:
            source._front = source._front._next
        source._count -=1
        self._rear._next = None
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        if source1._count > source2._count:
            count = source1._count
        else:
            count = source2._count
        i = 0
        while i < count:
            if source1._count != 0:
                self._move_front_to_rear(source1)
            if source2._count != 0:
                self._move_front_to_rear(source2)
            i +=1
        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine_r(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        self._combine_r_aux(source1, source2)
        return
    def _combine_r_aux(self, source1, source2):
        if source1._front is not None or source2._front is not None:
            if source1._front is not None:
                self._move_front_to_rear(source1)
            if source2._front is not None:
                self._move_front_to_rear(source2)
            if source1._front is not None or source2._front is not None:
                self._combine_r_aux(source1, source2) 

        return
            

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next

