class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        total_endtime = int(endTime[:2])*60*60+int(endTime[3:5])*60+int(endTime[6:])
        total_starttime = int(startTime[:2])*60*60+int(startTime[3:5])*60+int(startTime[6:])
        return abs(total_endtime - total_starttime)