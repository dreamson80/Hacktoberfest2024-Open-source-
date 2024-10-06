def count_columns_with_all_colors(n, rings):
    # دیکشنری برای ذخیره رنگ‌های حلقه‌ها در هر ستون
    columns = {i: set() for i in range(10)}
    
    # پر کردن دیکشنری با رنگ‌های هر ستون
    for ring in rings:
        color, column = ring[0], int(ring[1])
        columns[column].add(color)
    
    # شمارش ستون‌هایی که هر سه رنگ را دارند
    count = 0
    for colors in columns.values():
        if {'B', 'G', 'W'}.issubset(colors):
            count += 1
    
    return count

# خواندن ورودی
n = int(input().strip())
rings = [input().strip() for _ in range(n)]

# چاپ نتیجه
print(count_columns_with_all_colors(n, rings))
