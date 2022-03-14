package main

import "log"

/*
 * Complete the 'dynamicArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

func dynamicArray(n int32, queries [][]int32) []int32 {
	var arr [][]int32
	var lastAnswer int32
	var answers []int32

	for i := int32(0); i < n; i++ {
		arr = append(arr, []int32{})
	}

	for _, query := range queries {
		idx := (query[1] ^ lastAnswer) % n
		switch query[0] {
		case 1:
			arr[idx] = append(arr[idx], query[2])
		case 2:
			lastAnswer = arr[idx][query[2]%int32(len(arr[idx]))]
			answers = append(answers, lastAnswer)
		}
	}
	return answers
}

func main() {
	var n int32 = 2

	queries := [][]int32{
		{1, 0, 5},
		{1, 1, 7},
		{1, 0, 3},
		{2, 1, 0},
		{2, 1, 1},
	}

	log.Println(dynamicArray(n, queries)) // [7, 3]
}
