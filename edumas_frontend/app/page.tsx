import Link from "next/link"
import { ArrowRight, BookOpen, GraduationCap, Users } from "lucide-react"

import { Button } from "@/components/ui/button"

export default function LandingPage() {
  return (
    <div className="flex min-h-screen w-full flex-col">
      {/* Navbar */}
      <header className="border-b bg-white w-full">
        <div className="flex h-16 items-center justify-between w-full px-4 md:px-6">
          <div className="flex items-center gap-2">
            <GraduationCap className="h-6 w-6 text-primary" />
            <span className="text-xl font-bold">Edumas</span>
          </div>
          <nav className="hidden gap-6 md:flex flex-1 justify-center">
            <Link href="#features" className="text-sm font-medium hover:underline">
              Features
            </Link>
            <Link href="#testimonials" className="text-sm font-medium hover:underline">
              Testimonials
            </Link>
            <Link href="#about" className="text-sm font-medium hover:underline">
              About
            </Link>
          </nav>
          <div className="flex items-center gap-4">
            <Link href="/auth/login">
              <Button variant="ghost" size="sm">
                Login
              </Button>
            </Link>
            <Link href="/auth/register">
              <Button size="sm">Register</Button>
            </Link>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="flex flex-1 items-center w-full bg-gradient-to-b from-white to-slate-50 py-20">
        <div className="w-full h-full">
          <div className="grid h-full gap-6 lg:grid-cols-2 lg:gap-12 px-4 md:px-6">
            <div className="flex flex-col justify-center space-y-4">
              <div className="space-y-2">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl">Simplify Education Management</h1>
                <p className="max-w-[600px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Our platform streamlines administrative tasks, enhances communication, and improves learning outcomes
                  for educational institutions.
                </p>
              </div>
              <div className="flex flex-col gap-2 min-[400px]:flex-row">
                <Link href="/auth/register">
                  <Button size="lg" className="gap-1.5">
                    Get Started
                    <ArrowRight className="h-4 w-4" />
                  </Button>
                </Link>
                <Link href="#features">
                  <Button size="lg" variant="outline">
                    Learn More
                  </Button>
                </Link>
              </div>
            </div>
            <div className="flex items-center justify-center">
              <img
                src="/placeholder.svg?height=400&width=500"
                alt="Education Management Dashboard"
                className="rounded-lg object-cover shadow-lg"
                width={500}
                height={400}
              />
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="w-full bg-white py-20">
        <div className="w-full">
          <div className="mb-12 text-center px-4 md:px-6">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl">Key Features</h2>
            <p className="mx-auto mt-4 max-w-[700px] text-gray-500 md:text-xl/relaxed">
              Everything you need to manage your educational institution efficiently.
            </p>
          </div>
          <div className="grid gap-8 px-4 md:px-6 sm:grid-cols-2 lg:grid-cols-3">
            <div className="flex flex-col items-center space-y-2 rounded-lg border p-6 shadow-sm">
              <div className="rounded-full bg-primary/10 p-3">
                <Users className="h-6 w-6 text-primary" />
              </div>
              <h3 className="text-xl font-bold">Student Management</h3>
              <p className="text-center text-gray-500">
                Easily manage student records, attendance, and performance tracking.
              </p>
            </div>
            <div className="flex flex-col items-center space-y-2 rounded-lg border p-6 shadow-sm">
              <div className="rounded-full bg-primary/10 p-3">
                <BookOpen className="h-6 w-6 text-primary" />
              </div>
              <h3 className="text-xl font-bold">Course Management</h3>
              <p className="text-center text-gray-500">
                Create and manage courses, assignments, and learning materials.
              </p>
            </div>
            <div className="flex flex-col items-center space-y-2 rounded-lg border p-6 shadow-sm">
              <div className="rounded-full bg-primary/10 p-3">
                <GraduationCap className="h-6 w-6 text-primary" />
              </div>
              <h3 className="text-xl font-bold">Grading System</h3>
              <p className="text-center text-gray-500">
                Comprehensive grading tools with customizable assessment criteria.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="w-full border-t bg-slate-50">
        <div className="w-full flex flex-col gap-4 py-10 px-4 md:px-6 md:flex-row md:items-center md:justify-between md:py-12">
          <div className="flex items-center gap-2">
            <GraduationCap className="h-6 w-6 text-primary" />
            <span className="text-xl font-bold">Edumas</span>
          </div>
          <p className="text-sm text-gray-500">© {new Date().getFullYear()} Edu. All rights reserved.</p>
          <div className="flex gap-4">
            <Link href="#" className="text-sm text-gray-500 hover:underline">
              Privacy Policy
            </Link>
            <Link href="#" className="text-sm text-gray-500 hover:underline">
              Terms of Service
            </Link>
          </div>
        </div>
      </footer>
    </div>
  )
}