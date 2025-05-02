"use client"

import { Layout } from "@/components/layout"
import { TaskCards } from "@/components/dashboard/task-cards"
import { MetricCards } from "@/components/dashboard/metric-cards"
import { PerformanceChart } from "@/components/dashboard/performance-chart"
import { ActivitiesTable } from "@/components/dashboard/activities-table"
import { StudentDistribution } from "@/components/dashboard/student-distribution"

export default function Dashboard() {
  return (
    <Layout>
      <h1 className="text-2xl font-bold mb-6">School Dashboard</h1>

      <TaskCards />
      <MetricCards />
      <PerformanceChart />

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <ActivitiesTable />
        </div>
        <div>
          <StudentDistribution />
        </div>
      </div>
    </Layout>
  )
}
