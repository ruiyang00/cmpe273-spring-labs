import os
import tempfile
import sys
import asyncio


class heapNode:

    def __init__(self, item, whichFile):
        self.item = item
        self.whichFile = whichFile


class externalSort:

    def __init__(self):
        self.disk = []

    def partition(self, arr, low, high):
        i = (low-1)         
        pivot = arr[high]    

        for j in range(low, high):

            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def quickSort(self, arr, low, high):
        if low < high:

            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)

    def initialFirstSorts(self, disk_path, total_files, memorySize):

        entiries = os.listdir(disk_path)
        tempBuffer = []

        for i in range(total_files):

        
            infile = open(disk_path+entiries[i], 'r')
            for line in infile:
                tempBuffer.append(line)
            infile.close()
            tempBuffer = sorted(tempBuffer, key=lambda no:
                                int(no.strip()))
            tempFile = tempfile.NamedTemporaryFile(dir=self.getDiskPath()
                                                   + '/diskFiles', delete=False, mode='w+')

            tempFile.writelines(tempBuffer)
            tempFile.seek(0)
            self.disk.append(tempFile)
            tempBuffer = []

    def getDiskPath(self):
        cwd = os.getcwd()
        return cwd


    async def mergeSortedFiles(self, disk_path, total_files):
        tempbuffer = []

        for sortedFile in self.disk:
            num = int(sortedFile.readline().strip())
            tempbuffer.append(heapNode(num, sortedFile))

        # sort the 10 size buffer
        tempbuffer.sort(key=lambda node: node.item)

        while True:

            min = tempbuffer.pop(0)
            if min.item == sys.maxsize:
                break
            await self.wrtieToDisk_2ndSort(min.item)
            # output_file.append(min.item)
            fileOfMinRemoved = min.whichFile
            item = await self.readFromDisk_2ndSort(fileOfMinRemoved)

            if not item:
                item = sys.maxsize
            else:
                item = int(item)
            tempbuffer.append(heapNode(item, fileOfMinRemoved))
            tempbuffer.sort(key=lambda node: node.item)

    async def readFromDisk_2ndSort(self, file):
        file.readline().strip()

    async def wrtieToDisk_2ndSort(self, min):
        f = open(self.getDiskPath() + "/output/async_sorted.txt", "a")
        f.write(str(min)+"\n")


if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    """ 1)sort the ten files from disk with memorySize = 100 """
    memorySize = 100
    numsOfFileToBeSorted = 10
    exs = externalSort()
    disk_path = exs.getDiskPath()
    exs.initialFirstSorts(disk_path + "/input/",
                          numsOfFileToBeSorted, memorySize)

    """ 2)merge the """
    loop.run_until_complete(exs.mergeSortedFiles(
        disk_path + "/diskFiles/", numsOfFileToBeSorted))

    loop.close()

# pages = []
# buffer = []

# for i in range(len(pages)):
#     for j in range(len(pages[i])):
#         print(pages[i][j])
