/* rotating an array approaches*/

func rotateArray(nums []int, rotationSize int){
	// getting length of array
	n := len(nums)
	for i := 0; i < n; i++ {
		newIndex := (i + rotationSize) % n
	}
}