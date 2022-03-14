package main

import (
	"log"
	"math"
)

/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

func hourglassSum(arr [][]int32) int32 {
	var maxValue int32 = math.MinInt32
	for i := 0; i <= 3; i++ {
		for j := 0; j <= 3; j++ {
			var value int32
			value += arr[i][j] + arr[i][j+1] + arr[i][j+2]
			value += arr[i+1][j+1]
			value += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
			if value > maxValue {
				maxValue = value
			}
		}
	}
	return maxValue
}

func main() {
	arr := [][]int32{
		{1, 1, 1, 0, 0, 0},
		{0, 1, 0, 0, 0, 0},
		{1, 1, 1, 0, 0, 0},
		{0, 0, 2, 4, 4, 0},
		{0, 0, 0, 2, 0, 0},
		{0, 0, 1, 2, 4, 0},
	}
	log.Println(hourglassSum(arr) == 19)
}
