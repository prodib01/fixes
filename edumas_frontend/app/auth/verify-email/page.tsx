"use client";

import { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import { GraduationCap } from "lucide-react";
import { VerifyEmailForm } from "@/components/auth/verify-email-form";
import { Alert, AlertDescription } from "@/components/ui/alert";

export default function VerifyEmailPage() {
  const searchParams = useSearchParams();
  const [email, setEmail] = useState("");

  useEffect(() => {
    const emailParam = searchParams.get("email");
    if (emailParam) {
      setEmail(emailParam);
    }
  }, [searchParams]);

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
            <h1 className="text-3xl font-bold">Verify Your Email</h1>
        {email ? (
          <div className="mb-4 text-center">
            <p className="text-sm text-muted-foreground">
              Please enter the verification code sent to:
            </p>
            <p className="font-sm">{email}</p>
          </div>
        ) : (
          <Alert variant="default" className="mb-4">
            <AlertDescription>
              Email address is missing. Please go back to registration.
            </AlertDescription>
          </Alert>
        )}
          </div>

          <VerifyEmailForm initialEmail={email} />

          <div className="mt-6 text-center text-sm">
            <Link
              href="/auth/login"
              className="font-medium text-primary underline underline-offset-4"
            >
              Back to Login
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
