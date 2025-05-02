import { Users, GraduationCap, BookOpen, BarChart2 } from "lucide-react"
import { Card, CardContent } from "@/components/ui/card"

export function MetricCards() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
      <Card>
        <CardContent className="p-4 flex justify-between items-center">
          <div>
            <p className="text-gray-500 text-sm">Total Students</p>
            <span className="text-xl font-bold">1,248</span>
          </div>
          <div className="bg-blue-100 p-2 rounded-md">
            <Users className="h-6 w-6 text-blue-500" />
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardContent className="p-4 flex justify-between items-center">
          <div>
            <p className="text-gray-500 text-sm">Total Teachers</p>
            <span className="text-xl font-bold">64</span>
          </div>
          <div className="bg-purple-100 p-2 rounded-md">
            <GraduationCap className="h-6 w-6 text-purple-500" />
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardContent className="p-4 flex justify-between items-center">
          <div>
            <p className="text-gray-500 text-sm">Total Classes</p>
            <span className="text-xl font-bold">42</span>
          </div>
          <div className="bg-orange-100 p-2 rounded-md">
            <BookOpen className="h-6 w-6 text-orange-500" />
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardContent className="p-4 flex justify-between items-center">
          <div>
            <p className="text-gray-500 text-sm">Attendance Rate</p>
            <span className="text-xl font-bold">94.2%</span>
          </div>
          <div className="bg-green-100 p-2 rounded-md">
            <BarChart2 className="h-6 w-6 text-green-500" />
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
