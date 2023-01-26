def reverse_item_at_index(n):    
    data = ['Alice', 'Bob', 'Charlie', 'Daisy', 'Ernie', 'Frank', 'Gob']
    x = data[n]     
    x = x[::-1]
    return x

print("first item:", reverse_item_at_index(0))
print("last item:", reverse_item_at_index(6))
print("after data end:", reverse_item_at_index(7))
print("after buffer end:", reverse_item_at_index(1024)) 
print("before buffer start:", reverse_item_at_index(-1))
