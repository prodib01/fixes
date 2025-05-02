import type { Metadata } from "next"
import Link from "next/link"
import { GraduationCap } from "lucide-react"

import { RegisterForm } from "@/components/auth/register-form"

export const metadata: Metadata = {
  title: "Register | Edumas",
  description: "Create a new Edumas account",
}

export default function RegisterPage() {
  return (
    <div className="flex min-h-screen w-full flex-col bg-slate-50">
      <div className="container flex h-16 items-center px-4 md:px-6">
        <Link href="/" className="flex items-center gap-2">
          <GraduationCap className="h-6 w-6 text-primary" />
          <span className="text-xl font-bold">Edumas</span>
        </Link>
      </div>
      <div className="flex flex-1 items-center justify-center px-4 py-12">
        <div className="mx-auto w-full max-w-lg">
          <RegisterForm />
        </div>
      </div>
    </div>
  )
}