import { Card, CardContent } from "@/components/ui/card"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

export function PerformanceChart() {
  return (
    <Card className="mb-8">
      <CardContent className="p-6">
        <div className="flex justify-between items-center mb-6">
          <div>
            <p className="text-gray-500 text-sm">Student Performance</p>
            <h2 className="text-3xl font-bold">78.6 Average</h2>
          </div>
          <Select defaultValue="semester">
            <SelectTrigger className="w-[150px]">
              <SelectValue placeholder="Select period" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="semester">Current Semester</SelectItem>
              <SelectItem value="year">Academic Year</SelectItem>
              <SelectItem value="quarter">Quarter</SelectItem>
            </SelectContent>
          </Select>
        </div>
        <div className="h-[200px] relative">
          <ChartSvg />
        </div>
        <div className="flex justify-between text-xs text-gray-500 mt-2">
          <span>Math</span>
          <span>Science</span>
          <span>English</span>
          <span>History</span>
          <span>Art</span>
          <span>Music</span>
          <span>P.E.</span>
          <span>Comp Sci</span>
          <span>Biology</span>
          <span>Chemistry</span>
          <span>Physics</span>
          <span>Languages</span>
        </div>
      </CardContent>
    </Card>
  )
}

function ChartSvg() {
  return (
    <svg className="w-full h-full" viewBox="0 0 800 200">
      <defs>
        <linearGradient id="gradient" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stopColor="#3b82f6" stopOpacity="0.2" />
          <stop offset="100%" stopColor="#3b82f6" stopOpacity="0" />
        </linearGradient>
      </defs>
      <path
        d="M0,80 C50,60 100,90 150,70 C200,50 250,30 300,50 C350,70 400,20 450,40 C500,60 550,90 600,70 C650,50 700,80 750,60 L750,200 L0,200 Z"
        fill="url(#gradient)"
      />
      <path
        d="M0,80 C50,60 100,90 150,70 C200,50 250,30 300,50 C350,70 400,20 450,40 C500,60 550,90 600,70 C650,50 700,80 750,60"
        fill="none"
        stroke="#3b82f6"
        strokeWidth="2"
      />
      <g className="y-axis">
        <text x="780" y="10" className="text-xs fill-gray-500">
          100
        </text>
        <text x="780" y="50" className="text-xs fill-gray-500">
          80
        </text>
        <text x="780" y="90" className="text-xs fill-gray-500">
          60
        </text>
        <text x="780" y="130" className="text-xs fill-gray-500">
          40
        </text>
        <text x="780" y="170" className="text-xs fill-gray-500">
          20
        </text>
        <text x="780" y="200" className="text-xs fill-gray-500">
          0
        </text>
      </g>
    </svg>
  )
}
