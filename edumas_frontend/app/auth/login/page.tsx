import type { Metadata } from "next"
import Link from "next/link"
import { GraduationCap } from "lucide-react"

import { LoginForm } from "@/components/auth/login-form"

export const metadata: Metadata = {
  title: "Login | Edumas",
  description: "Login to your Edumas account",
}

export default function LoginPage() {
  return (
    <div className="flex min-h-screen w-full flex-col bg-slate-50">
      <div className="container flex h-16 items-center px-4 md:px-6">
        <Link href="/" className="flex items-center gap-2">
          <GraduationCap className="h-6 w-6 text-primary" />
          <span className="text-xl font-bold">Edumas</span>
        </Link>
      </div>
      <div className="flex flex-1 items-center justify-center px-4 py-12">
        <div className="mx-auto w-full max-w-md">
          <div className="mb-6 space-y-2 text-center">
            <h1 className="text-3xl font-bold">Login</h1>
            <p className="text-gray-500">Enter your credentials to access your account</p>
          </div>
          <LoginForm />
          <div className="mt-6 text-center text-sm">
            Don&apos;t have an account?{" "}
            <Link href="/auth/register" className="font-medium text-primary underline underline-offset-4">
              Register
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}
