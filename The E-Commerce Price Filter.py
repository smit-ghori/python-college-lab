# h2) The E-Commerce Price Filter (First occurrence ≥ target)

# You're on Flipkart. You filter products: "Show me laptops priced ₹50,000 or above." Products are sorted by price. Flipkart must find the first product whose price is greater than or equal to ₹50,000 using Binary Search (Lower Bound).

# Question:
# Write a program to find the first occurrence of an element greater than or equal to a given target in a sorted array using Binary Search (Lower Bound).

prices = [25000, 35000, 42000, 48000, 65000, 70000]
target = 50000

start = 0
end = len(prices) - 1
answer = -1

while start <= end:
    mid = (start + end) // 2
    if prices[mid] <= target:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid


if answer != -1:
    print("Index:", answer)
    print("Price:", prices[answer])
else:
    print("No product found.")
