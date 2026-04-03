func isAnagram(s string, t string) bool {
   if len(s) != len(t){
        return false
   }

   holder:= make(map[rune]int)

   for _,ch := range s{
        holder[ch]++
   }
   for _,ch := range t{
    holder[ch]--
    if holder[ch]<0{
        return false
    }
   }

   return true

}
