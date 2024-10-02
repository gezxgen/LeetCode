int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    *returnSize=2;
    int *arr = malloc(2*sizeof(int));

    for (int i=0; i<numsSize; i++) {
        for(int j=1+i; j<numsSize; j++) {
            if(nums[i] + nums[j] == target) {
            arr[0] = i;
            arr[1] = j;
            return arr;
            }
        }
    }
    return NULL;
}