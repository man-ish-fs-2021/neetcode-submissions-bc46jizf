class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals) {
        intervals.sort((a,b) => a[0] - b[0])
        const output = [intervals[0]]

        for (let [start,end] of intervals){
            console.log({start, end})
            let lastEnd = output[output.length - 1 ][1]

            if (start <= lastEnd){
                output[output.length - 1 ][1] = Math.max(end, lastEnd)
            } else {
                output.push([start, end])
            }


        }
        return output
    }
}
