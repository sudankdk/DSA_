func groupAnagrams(strs []string) [][]string {
	hash := make(map[string][]string)

	for _,v := range strs {
		b := []byte(v)

		sort.Slice(b,func(i,j int)bool {
			return b[i]<b[j]
		})

		key := string(b)
		hash[key]= append(hash[key],v)

	}

	result := make([][]string,0,len(hash))
	for _,groups := range hash{
		result = append(result,groups)
	}
	return result
}