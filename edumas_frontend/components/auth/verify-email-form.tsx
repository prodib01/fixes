"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { authAPI, setLocalStorageConfigs } from "@/lib/api";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { Card, CardContent, CardFooter } from "@/components/ui/card";
import { IUserProfile } from "@/lib/types";

// Add props type
interface VerifyEmailFormProps {
  initialEmail?: string;
}

export function VerifyEmailForm({ initialEmail = "" }: VerifyEmailFormProps) {
  const router = useRouter();

  const [email, setEmail] = useState(initialEmail);
  const [otp, setOtp] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);

  // In case the prop changes dynamically
  useEffect(() => {
    setEmail(initialEmail);
  }, [initialEmail]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!email) {
      setError("Email is required. Please try again or contact support.");
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const response: any = await authAPI.verifyEmail(email, otp);
      const user: IUserProfile = response.user_profile;

      if (response.access) {
        setLocalStorageConfigs(response.access, response.user_profile);
      }

      setSuccess("Email verified successfully! Redirecting to dashboard...");

      setTimeout(() => {
        if (user.user_type === "school_owner") {
          router.push("/schools/create");
        } else {
          router.push("/dashboard");
        }
      }, 2000);
    } catch (err: any) {
      setError(err.message || "Failed to verify email. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleResendVerification = async () => {
    if (!email) {
      setError(
        "Email address is missing. Please try again or contact support."
      );
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      await authAPI.resendVerification(email);
      setSuccess("Verification code sent to your email address");
      setTimeout(() => setSuccess(null), 3000);
    } catch (err: any) {
      setError(err.message || "Failed to resend verification code");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Card className="w-full shadow-md">
      <CardContent>
        {error && (
          <Alert variant="destructive" className="mb-4">
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        )}

        {success && (
          <Alert className="mb-4">
            <AlertDescription>{success}</AlertDescription>
          </Alert>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="space-y-2">
            <label htmlFor="otp" className="text-sm font-medium">
              Verification Code
            </label>
            <Input
              id="otp"
              type="text"
              placeholder="Enter verification code"
              value={otp}
              onChange={(e) => setOtp(e.target.value)}
              required
              autoFocus
            />
          </div>
          <Button type="submit" className="w-full" disabled={isLoading}>
            {isLoading ? "Verifying..." : "Verify Email"}
          </Button>
        </form>
      </CardContent>
      <CardFooter className="flex justify-center border-t pt-4">
        <button
          type="button"
          onClick={handleResendVerification}
          className="text-sm text-primary hover:underline"
          disabled={isLoading}
        >
          Didn&apos;t receive a code? Resend
        </button>
      </CardFooter>
    </Card>
  );
}
