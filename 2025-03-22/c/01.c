#include <stdio.h>

// In an array, there is an element only occouring once
// Other elements occour multiple times
// Find that element in O(n) time

void main()
{
    int arr[] = {1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    // Trainer - Use a sliding window
    // I dont get how this is the better way
    for (int i = 0; i < n - 1; i++)
    {
        if (arr[i] != arr[i + 1] && arr[i] != arr[i + 2])
        {
            printf("Element occurring only once: %d\n", arr[i]);
            break;
        }
        else if (arr[i + 1] != arr[i] && arr[i + 1] != arr[i + 2])
        {
            printf("Element occurring only once: %d\n", arr[i + 1]);
            break;
        }
        else
        {
            printf("Element occurring only once: %d\n", arr[i + 2]);
            break;
        }
    }
}