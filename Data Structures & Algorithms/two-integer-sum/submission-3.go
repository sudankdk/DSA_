func twoSum(nums []int, target int) []int {
    hash := make(map[int]int)
    for i,v := range nums {
        num := target -v
        if n, ok := hash[num];ok {
            return []int{n,i}
        }else{
            hash[v]=i
        }
    }
    return []int{-1,-1}
}
