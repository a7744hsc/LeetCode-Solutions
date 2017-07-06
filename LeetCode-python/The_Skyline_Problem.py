class Solution(object):
    def array_autoincrement(self,arr,last_index):
        if len(arr) <= last_index:
            arr.extend(0 for i in range(last_index+2-len(arr)))

    def getSkyline(self, buildings):
        landscape = []
        output = []
        point_map = {}
        for building in buildings:
            if building[0] not in point_map:
                point_map[building[0]]=building[2]
            else:
                point_map[building[0]] = point_map[building[0]] if point_map[building[0]] >building[2] else building[2]

            if building[1] not in  point_map:
                point_map[building[1]]=0
            else:
                point_map[building[1]] = point_map[building[1]] if point_map[building[1]] > 0 else 0

        key_to_delete = []

        for pos in point_map.keys():
            height = point_map.get(pos)
            height_candidate = 0;
            for building2 in buildings:
                if building2[0] <= pos and building2[1]>pos and building2[2]>height:
                    if height !=0:
                        key_to_delete.append(pos)
                        break
                    elif height_candidate<building2[2]:
                        height_candidate = building2[2]
            if height == 0 and height_candidate != 0 :
                point_map[pos] = height_candidate;

                    # height = building2[2]
            # point_map[pos]=height

        for x in key_to_delete:
            del point_map[x]

        sorted_keys = sorted(point_map.keys())

        pre_height = 0
        for k in sorted_keys:
            height = point_map[k]
            if height != pre_height:
                output.append([k,height])
                pre_height = height


        return output

if __name__ == '__main__':
    # a= [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    a= [[2,4,7],[2,4,5],[2,4,6]]
    s = Solution()
    result = s.getSkyline(a)
    print(a)