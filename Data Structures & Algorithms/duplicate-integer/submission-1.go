func hasDuplicate(nums []int) bool {
    a:= make(map[int]int)
    for i,v:=range nums{
        _,ok:=a[v]
        if ok {
            return true
        }else {
            a[v]=i
        }
    }
    return false
}
