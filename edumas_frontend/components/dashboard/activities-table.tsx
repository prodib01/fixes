import { ChevronRight } from "lucide-react"
import Link from "next/link"
import { Card, CardContent } from "@/components/ui/card"

export function ActivitiesTable() {
  return (
    <div>
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-bold">Recent Activities</h2>
        <Link href="#" className="text-blue-500 text-sm flex items-center">
          View all activities
          <ChevronRight className="h-4 w-4 ml-1" />
        </Link>
      </div>
      <Card>
        <CardContent className="p-0">
          <table className="w-full">
            <thead className="bg-gray-50 border-b">
              <tr>
                <th className="text-left p-4 text-sm font-medium text-gray-500">Activity</th>
                <th className="text-left p-4 text-sm font-medium text-gray-500">Student</th>
                <th className="text-left p-4 text-sm font-medium text-gray-500">Class</th>
                <th className="text-left p-4 text-sm font-medium text-gray-500">Date</th>
              </tr>
            </thead>
            <tbody>
              <tr className="border-b">
                <td className="p-4 text-sm">Assignment Submitted</td>
                <td className="p-4 text-sm">John Smith</td>
                <td className="p-4 text-sm">Mathematics 101</td>
                <td className="p-4 text-sm">25 Apr 2025, 4:34 pm</td>
              </tr>
              <tr className="border-b">
                <td className="p-4 text-sm">Attendance Marked</td>
                <td className="p-4 text-sm">Sarah Johnson</td>
                <td className="p-4 text-sm">Biology 202</td>
                <td className="p-4 text-sm">25 Apr 2025, 9:15 am</td>
              </tr>
              <tr>
                <td className="p-4 text-sm">Grade Updated</td>
                <td className="p-4 text-sm">Michael Brown</td>
                <td className="p-4 text-sm">History 303</td>
                <td className="p-4 text-sm">24 Apr 2025, 2:45 pm</td>
              </tr>
            </tbody>
          </table>
        </CardContent>
      </Card>
    </div>
  )
}
