"use client"

import type React from "react"

import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import { isAuthenticated, getToken } from "@/lib/api"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { AlertCircle, CheckCircle2, Loader2 } from "lucide-react"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"

interface SchoolFormData {
  name: string
  address: string
  city: string
  state: string
  country: string
  phone: string
  email: string
  website?: string
  description?: string
  school_type: string
}

export default function CreateSchool() {
  const router = useRouter()
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [success, setSuccess] = useState<string | null>(null)
  const [submitting, setSubmitting] = useState(false)
  const [userData, setUserData] = useState<any>(null)

  const [formData, setFormData] = useState<SchoolFormData>({
    name: "",
    address: "",
    city: "",
    state: "",
    country: "",
    phone: "",
    email: "",
    website: "",
    description: "",
    school_type: "primary",
  })

  useEffect(() => {
    // Check if user is authenticated
    if (!isAuthenticated()) {
      router.push("/auth/login")
      return
    }

    // Verify user type from token
    const checkUserType = async () => {
      try {
        const token = getToken()
        if (!token) {
          throw new Error("Authentication required")
        }

        // Simulating getting user data from token or API
        const userData = await fetchUserData() as { user_type: string }
        setUserData(userData)

        // Check if user is a school owner
        if ((userData as { user_type: string }).user_type !== "school_owner") {
          router.push("/dashboard")
          setError("Only school owners can create schools")
        }

        setLoading(false)
      } catch (err: any) {
        setError(err.message || "Failed to verify user")
        setLoading(false)
      }
    }

    checkUserType()
  }, [router])

  // Simulated function to fetch user data
  const fetchUserData = async () => {
    // In a real app, you would make an API call here
    // For this example, we're simulating the response
    return new Promise((resolve) => {
      setTimeout(() => {
        // Simulating the user data returned from the API
        resolve({
          id: "123",
          email: "user@example.com",
          user_type: "school_owner",
          name: "John Doe",
          email_verified: true,
        })
      }, 1000)
    })
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target
    setFormData((prev) => ({ ...prev, [name]: value }))
  }

  const handleSelectChange = (name: string, value: string) => {
    setFormData((prev) => ({ ...prev, [name]: value }))
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setSubmitting(true)
    setError(null)
    setSuccess(null)

    try {
      // In a real app, you would make an API call to create the school
      // For example:
      // const response = await apiRequest('/schools/', 'POST', formData)

      // Simulating API call
      await new Promise((resolve) => setTimeout(resolve, 2000))

      setSuccess("School created successfully!")

      // Redirect to school dashboard after a short delay
      setTimeout(() => {
        router.push("/school/dashboard")
      }, 2000)
    } catch (err: any) {
      setError(err.message || "Failed to create school")
    } finally {
      setSubmitting(false)
    }
  }

  if (loading) {
    return (
      <div className="flex h-screen items-center justify-center">
        <Loader2 className="h-8 w-8 animate-spin text-primary" />
        <span className="ml-2">Verifying user...</span>
      </div>
    )
  }

  if (error && error.includes("Only school owners")) {
    return (
      <div className="container mx-auto max-w-md p-6">
        <Alert variant="destructive">
          <AlertCircle className="h-4 w-4" />
          <AlertTitle>Access Denied</AlertTitle>
          <AlertDescription>{error}. You will be redirected to the dashboard.</AlertDescription>
        </Alert>
      </div>
    )
  }

  return (
    <div className="container mx-auto py-10">
      <Card className="max-w-3xl mx-auto">
        <CardHeader>
          <CardTitle className="text-2xl">Create Your School</CardTitle>
          <CardDescription>Fill in the details below to set up your school on our platform.</CardDescription>
        </CardHeader>
        <CardContent>
          {error && (
            <Alert variant="destructive" className="mb-6">
              <AlertCircle className="h-4 w-4" />
              <AlertTitle>Error</AlertTitle>
              <AlertDescription>{error}</AlertDescription>
            </Alert>
          )}

          {success && (
            <Alert className="mb-6 bg-green-50 border-green-200">
              <CheckCircle2 className="h-4 w-4 text-green-600" />
              <AlertTitle className="text-green-800">Success</AlertTitle>
              <AlertDescription className="text-green-700">{success}</AlertDescription>
            </Alert>
          )}

          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="space-y-4">
              <div>
                <Label htmlFor="name">School Name *</Label>
                <Input
                  id="name"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  required
                  placeholder="Enter school name"
                />
              </div>

              <div>
                <Label htmlFor="school_type">School Type *</Label>
                <Select
                  value={formData.school_type}
                  onValueChange={(value) => handleSelectChange("school_type", value)}
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Select school type" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="primary">Primary School</SelectItem>
                    <SelectItem value="secondary">Secondary School</SelectItem>
                    <SelectItem value="high">High School</SelectItem>
                    <SelectItem value="college">College</SelectItem>
                    <SelectItem value="university">University</SelectItem>
                    <SelectItem value="vocational">Vocational School</SelectItem>
                    <SelectItem value="other">Other</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
                <div>
                  <Label htmlFor="email">School Email *</Label>
                  <Input
                    id="email"
                    name="email"
                    type="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                    placeholder="school@example.com"
                  />
                </div>
                <div>
                  <Label htmlFor="phone">School Phone *</Label>
                  <Input
                    id="phone"
                    name="phone"
                    value={formData.phone}
                    onChange={handleChange}
                    required
                    placeholder="+1234567890"
                  />
                </div>
              </div>

              <div>
                <Label htmlFor="website">School Website</Label>
                <Input
                  id="website"
                  name="website"
                  value={formData.website}
                  onChange={handleChange}
                  placeholder="https://www.yourschool.com"
                />
              </div>

              <div>
                <Label htmlFor="address">Address *</Label>
                <Input
                  id="address"
                  name="address"
                  value={formData.address}
                  onChange={handleChange}
                  required
                  placeholder="123 Education Street"
                />
              </div>

              <div className="grid grid-cols-1 gap-4 md:grid-cols-3">
                <div>
                  <Label htmlFor="city">City *</Label>
                  <Input
                    id="city"
                    name="city"
                    value={formData.city}
                    onChange={handleChange}
                    required
                    placeholder="City"
                  />
                </div>
                <div>
                  <Label htmlFor="state">State/Province *</Label>
                  <Input
                    id="state"
                    name="state"
                    value={formData.state}
                    onChange={handleChange}
                    required
                    placeholder="State/Province"
                  />
                </div>
                <div>
                  <Label htmlFor="country">Country *</Label>
                  <Input
                    id="country"
                    name="country"
                    value={formData.country}
                    onChange={handleChange}
                    required
                    placeholder="Country"
                  />
                </div>
              </div>

              <div>
                <Label htmlFor="description">School Description</Label>
                <Textarea
                  id="description"
                  name="description"
                  value={formData.description}
                  onChange={handleChange}
                  placeholder="Tell us about your school..."
                  rows={4}
                />
              </div>
            </div>
          </form>
        </CardContent>
        <CardFooter className="flex justify-between">
          <Button variant="outline" onClick={() => router.back()}>
            Cancel
          </Button>
          <Button onClick={handleSubmit} disabled={submitting}>
            {submitting ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Creating...
              </>
            ) : (
              "Create School"
            )}
          </Button>
        </CardFooter>
      </Card>
    </div>
  )
}
