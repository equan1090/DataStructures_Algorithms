// function mergeSort(array) {
//     if (array.length <= 1) return array

//     const middleIdx = Math.floor(array.length / 2)
//     const leftIdx = array.slice(0, middleIdx)
//     const rightIdx = array.slice(middleIdx)

//     return mergeSortedArrays(mergeSort(leftIdx), mergeSort(rightIdx))
// }

// function mergeSortedArrays(leftHalf, rightHalf) {
//     const sortedArray = new Array(leftHalf.length + rightHalf.length)
//     let k = 0
//     let i = 0
//     let j = 0

//     while (i < leftHalf.length && j < rightHalf.length) {
//         if(leftHalf[i] <= rightHalf[j]) {
//             sortedArray[k++] = leftHalf[i++]
//         }else {
//             sortedArray[k++] = rightHalf[j++]
//         }
//     }

//     while (i < leftHalf.length) {
//         sortedArray[k++] = leftHalf[i++]
//     }
//     while (i < rightHalf.length) {
//         sortedArray[k++] = rightHalf[j++]
//     }
//     return sortedArray
// }
// console.log(mergeSort([2, 1 , 3, 9, 1, 8]))

function merge(left, right, count) {
    let array = []

    while (left.length && right.length) {

        if (left[0] < right[0]) {
            array.push(left.shift())
            count++
            console.log(count, 'in left')
        } else {
            array.push(right.shift())
            count++
            console.log(count, 'in right')
        }
    }

    return [ ...array, ...left, ...right]


}


function largestCountValue(a, count=0) {

    let half = a.length / 2

    if(a.length < 2){
      return a
    }

    let left = a.splice(0, half)
    return merge(largestCountValue(left),largestCountValue(a), count)



}

console.log(largestCountValue([1, 2, 3, 5, 2, 1]))
