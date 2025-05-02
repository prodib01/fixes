import { Card, CardContent } from "@/components/ui/card"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

export function SalesChart() {
  return (
    <Card className="mb-8">
      <CardContent className="p-6">
        <div className="flex justify-between items-center mb-6">
          <div>
            <p className="text-gray-500 text-sm">Sales</p>
            <h2 className="text-3xl font-bold">UGX 12,230,000</h2>
          </div>
          <Select defaultValue="annually">
            <SelectTrigger className="w-[150px]">
              <SelectValue placeholder="Select period" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="annually">Annually</SelectItem>
              <SelectItem value="monthly">Monthly</SelectItem>
              <SelectItem value="weekly">Weekly</SelectItem>
            </SelectContent>
          </Select>
        </div>
        <div className="h-[200px] relative">
          <ChartSvg />
        </div>
        <div className="flex justify-between text-xs text-gray-500 mt-2">
          <span>JAN</span>
          <span>FEB</span>
          <span>MAR</span>
          <span>APR</span>
          <span>MAY</span>
          <span>JUN</span>
          <span>JUL</span>
          <span>AUG</span>
          <span>SEP</span>
          <span>OCT</span>
          <span>NOV</span>
          <span>DEC</span>
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
          <stop offset="0%" stopColor="#22c55e" stopOpacity="0.2" />
          <stop offset="100%" stopColor="#22c55e" stopOpacity="0" />
        </linearGradient>
      </defs>
      <path
        d="M0,150 C50,120 100,180 150,140 C200,100 250,60 300,80 C350,100 400,40 450,60 C500,80 550,120 600,100 C650,80 700,120 750,110 L750,200 L0,200 Z"
        fill="url(#gradient)"
      />
      <path
        d="M0,150 C50,120 100,180 150,140 C200,100 250,60 300,80 C350,100 400,40 450,60 C500,80 550,120 600,100 C650,80 700,120 750,110"
        fill="none"
        stroke="#22c55e"
        strokeWidth="2"
      />
      <g className="y-axis">
        <text x="780" y="10" className="text-xs fill-gray-500">
          5M
        </text>
        <text x="780" y="50" className="text-xs fill-gray-500">
          4M
        </text>
        <text x="780" y="90" className="text-xs fill-gray-500">
          3M
        </text>
        <text x="780" y="130" className="text-xs fill-gray-500">
          2M
        </text>
        <text x="780" y="170" className="text-xs fill-gray-500">
          1M
        </text>
        <text x="780" y="200" className="text-xs fill-gray-500">
          0
        </text>
      </g>
    </svg>
  )
}
