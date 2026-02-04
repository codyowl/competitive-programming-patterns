package main


import (
	"fmt"
)

var nums = []int{1,2,3,4,0,0}

func replaceElements(nums []int) []int {
	writeIndex := 0
	for i := 0; i<len(nums); i++ {
		
		if nums[i] != 0 {
			fmt.Printf("yeah the current element %d is not eqal to 0\n", nums[i])
			nums[writeIndex] = nums[i]
			fmt.Println("Write Index value:",writeIndex)
			writeIndex ++
		}
	}
	return nums
}



func main (){
	replaceElements(nums)
}