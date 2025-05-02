"use client"

import {
  BookOpen,
  ChevronLeft,
  ChevronRight,
  GraduationCap,
  Home,
  Users,
  Calendar,
  ClipboardList,
  Award,
  Settings,
} from "lucide-react"
import Link from "next/link"
import { Button } from "@/components/ui/button"

interface SidebarProps {
  collapsed: boolean
  onToggle: () => void
}

export function Sidebar({ collapsed, onToggle }: SidebarProps) {
  return (
    <aside
      className={`h-screen bg-white border-r flex flex-col transition-all duration-300 ${
        collapsed ? "w-[70px]" : "w-[240px]"
      }`}
    >
      <div className={`flex items-center ${collapsed ? "justify-center" : "justify-between"} p-4 border-b`}>
        {!collapsed && (
          <div className="flex items-center">
            <div className="bg-blue-500 text-white p-2 rounded-md mr-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M22 10v6M2 10l10-5 10 5-10 5z" />
                <path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5" />
              </svg>
            </div>
            <h1 className="font-bold text-lg">SCHOOL</h1>
          </div>
        )}
        {collapsed && (
          <div className="bg-blue-500 text-white p-2 rounded-md">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M22 10v6M2 10l10-5 10 5-10 5z" />
              <path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5" />
            </svg>
          </div>
        )}
        <Button variant="ghost" size="sm" className="rounded-full p-1" onClick={onToggle}>
          {collapsed ? <ChevronRight size={18} /> : <ChevronLeft size={18} />}
        </Button>
      </div>

      <nav className="p-2 space-y-1 flex-1 overflow-y-auto">
        <Link
          href="#"
          className={`flex items-center gap-3 bg-blue-500 text-white p-3 rounded-md ${
            collapsed ? "justify-center" : ""
          }`}
        >
          <Home className="h-5 w-5 flex-shrink-0" />
          {!collapsed && <span>Dashboard</span>}
        </Link>

        <Link
          href="#"
          className={`flex items-center gap-3 text-gray-700 p-3 rounded-md hover:bg-gray-100 ${
            collapsed ? "justify-center" : ""
          }`}
        >
          <Users className="h-5 w-5 flex-shrink-0" />
          {!collapsed && <span>Students</span>}
        </Link>

        <Link
          href="#"
          className={`flex items-center gap-3 text-gray-700 p-3 rounded-md hover:bg-gray-100 ${
            collapsed ? "justify-center" : ""
          }`}
        >
          <GraduationCap className="h-5 w-5 flex-shrink-0" />
          {!collapsed && <span>Teachers</span>}
        </Link>

        <Link
          href="#"
          className={`flex items-center gap-3 text-gray-700 p-3 rounded-md hover:bg-gray-100 ${
            collapsed ? "justify-center" : ""
          }`}
        >
          <BookOpen className="h-5 w-5 flex-shrink-0" />
          {!collapsed && <span>Classes</span>}
        </Link>

        <Link
          href="#"
          className={`flex items-center gap-3 text-gray-700 p-3 rounded-md hover:bg-gray-100 ${
            collapsed ? "justify-center" : ""
          }`}
        >
          <ClipboardList className="h-5 w-5 flex-shrink-0" />
          {!collapsed && <span>Attendance</span>}
        </Link>

        <Link
          href="#"
          className={`flex items-center gap-3 text-gray-700 p-3 rounded-md hover:bg-gray-100 ${
            collapsed ? "justify-center" : ""
          }`}
        >
          <Award className="h-5 w-5 flex-shrink-0" />
          {!collapsed && <span>Grades</span>}
        </Link>

        <Link
          href="#"
          className={`flex items-center gap-3 text-gray-700 p-3 rounded-md hover:bg-gray-100 ${
            collapsed ? "justify-center" : ""
          }`}
        >
          <Calendar className="h-5 w-5 flex-shrink-0" />
          {!collapsed && <span>Schedule</span>}
        </Link>
      </nav>

      <div className={`p-4 border-t ${collapsed ? "flex justify-center" : ""}`}>
        <div className={`flex items-center gap-3 text-gray-500 ${collapsed ? "" : ""}`}>
          <Settings className="h-5 w-5 flex-shrink-0" />
          {!collapsed && <span>Settings</span>}
        </div>
      </div>
    </aside>
  )
}
