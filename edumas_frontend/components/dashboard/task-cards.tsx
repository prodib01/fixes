import { ChevronRight } from "lucide-react"
import { Card, CardContent } from "@/components/ui/card"

export function TaskCards() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
      <Card className="bg-red-50 border-none">
        <CardContent className="p-4 flex justify-between items-center">
          <div>
            <span className="text-red-500 text-2xl font-bold">12</span>
            <p className="text-red-500">Absent Students</p>
          </div>
          <ChevronRight className="text-red-500" />
        </CardContent>
      </Card>

      <Card className="bg-blue-50 border-none">
        <CardContent className="p-4 flex justify-between items-center">
          <div>
            <span className="text-blue-500 text-2xl font-bold">8</span>
            <p className="text-blue-500">Pending Assignments</p>
          </div>
          <ChevronRight className="text-blue-500" />
        </CardContent>
      </Card>

      <Card className="bg-purple-50 border-none">
        <CardContent className="p-4 flex justify-between items-center">
          <div>
            <span className="text-purple-500 text-2xl font-bold">3</span>
            <p className="text-purple-500">Upcoming Events</p>
          </div>
          <ChevronRight className="text-purple-500" />
        </CardContent>
      </Card>

      <Card className="bg-green-50 border-none">
        <CardContent className="p-4 flex justify-between items-center">
          <div>
            <span className="text-green-500 text-2xl font-bold">24</span>
            <p className="text-green-500">Active Courses</p>
          </div>
          <ChevronRight className="text-green-500" />
        </CardContent>
      </Card>
    </div>
  )
}
