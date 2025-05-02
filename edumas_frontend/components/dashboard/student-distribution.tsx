import { Card, CardContent } from "@/components/ui/card"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

export function StudentDistribution() {
  return (
    <div>
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-bold">Student Distribution</h2>
        <Select defaultValue="grade">
          <SelectTrigger className="w-[120px]">
            <SelectValue placeholder="View by" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="grade">By Grade</SelectItem>
            <SelectItem value="gender">By Gender</SelectItem>
            <SelectItem value="age">By Age</SelectItem>
          </SelectContent>
        </Select>
      </div>
      <Card>
        <CardContent className="p-6 flex flex-col items-center">
          <div className="relative w-40 h-40 mb-4">
            <DonutChart />
          </div>
          <div className="text-center">
            <p className="text-sm text-gray-500">Total Students</p>
            <p className="text-2xl font-bold">1,248</p>
          </div>
          <div className="grid grid-cols-2 gap-2 w-full mt-4">
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded-full bg-blue-500"></div>
              <span className="text-sm">Grade 9: 312</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded-full bg-green-500"></div>
              <span className="text-sm">Grade 10: 298</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
              <span className="text-sm">Grade 11: 324</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded-full bg-purple-500"></div>
              <span className="text-sm">Grade 12: 314</span>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}

function DonutChart() {
  return (
    <svg className="w-full h-full" viewBox="0 0 100 100">
      {/* Background circle */}
      <circle cx="50" cy="50" r="40" fill="none" stroke="#f3f4f6" strokeWidth="15" />

      {/* Grade 9 - Blue */}
      <circle
        cx="50"
        cy="50"
        r="40"
        fill="none"
        stroke="#3b82f6"
        strokeWidth="15"
        strokeDasharray="80 220"
        strokeDashoffset="0"
        transform="rotate(-90 50 50)"
      />

      {/* Grade 10 - Green */}
      <circle
        cx="50"
        cy="50"
        r="40"
        fill="none"
        stroke="#22c55e"
        strokeWidth="15"
        strokeDasharray="75 225"
        strokeDashoffset="-80"
        transform="rotate(-90 50 50)"
      />

      {/* Grade 11 - Yellow */}
      <circle
        cx="50"
        cy="50"
        r="40"
        fill="none"
        stroke="#eab308"
        strokeWidth="15"
        strokeDasharray="82 218"
        strokeDashoffset="-155"
        transform="rotate(-90 50 50)"
      />

      {/* Grade 12 - Purple */}
      <circle
        cx="50"
        cy="50"
        r="40"
        fill="none"
        stroke="#a855f7"
        strokeWidth="15"
        strokeDasharray="78 222"
        strokeDashoffset="-237"
        transform="rotate(-90 50 50)"
      />
    </svg>
  )
}
