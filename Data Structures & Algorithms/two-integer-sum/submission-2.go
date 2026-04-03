func twoSum(nums []int, target int) []int {
    holder:= make(map[int]int)

    for i,v := range nums{
       newV := target- v
       _,ok:=holder[newV]
       if ok{
        return []int{holder[newV],i}
       }else{
        holder[v]=i
       }
    }

    return []int{-1,-1}
}
