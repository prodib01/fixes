"use client"

import type React from "react"
import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import { isAuthenticated, getToken, schoolAPI, campusAPI } from "@/lib/api"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import {
  AlertCircle,
  CheckCircle2,
  Loader2,
  ArrowRight,
  ArrowLeft,
  School,
  Building2,
  Mail,
  MapPin,
  CheckCircle,
} from "lucide-react"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { motion, AnimatePresence } from "framer-motion"

// Define the steps for our form
const steps = [
  { id: 1, name: "School Information", description: "Create your school", icon: School },
  { id: 2, name: "Campus Basic Info", description: "Name and type", icon: Building2 },
  { id: 3, name: "Campus Contact", description: "Contact information", icon: Mail },
  { id: 4, name: "Campus Location", description: "Address details", icon: MapPin },
  { id: 5, name: "Review & Submit", description: "Confirm your details", icon: CheckCircle },
]

// Animation variants for form transitions
const formVariants = {
  hidden: { opacity: 0, x: 50 },
  visible: { opacity: 1, x: 0, transition: { duration: 0.3 } },
  exit: { opacity: 0, x: -50, transition: { duration: 0.3 } },
}

interface SchoolFormData {
  name: string
}

interface CampusFormData {
  name: string
  code: string
  school_type: string
  category: string
  email: string
  phone: string
  website: string
  address: string
  city: string
  state: string
  country: string
  is_active: boolean
  school: number | null
}

export default function CreateSchool() {
  const router = useRouter()
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [success, setSuccess] = useState<string | null>(null)
  const [submitting, setSubmitting] = useState(false)
  const [userData, setUserData] = useState<any>(null)
  const [currentStep, setCurrentStep] = useState(1)
  const [completedSteps, setCompletedSteps] = useState<number[]>([])
  const [createdSchool, setCreatedSchool] = useState<any>(null)

  // Form data for school creation
  const [schoolFormData, setSchoolFormData] = useState<SchoolFormData>({
    name: "",
  })

  // Form data for campus creation
  const [campusFormData, setCampusFormData] = useState<CampusFormData>({
    name: "",
    code: "",
    school_type: "secondary",
    category: "mixed",
    email: "",
    phone: "",
    website: "",
    address: "",
    city: "",
    state: "",
    country: "",
    is_active: true,
    school: null,
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
        const userData = (await fetchUserData()) as { user_type: string }
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

  const handleSchoolChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target
    setSchoolFormData((prev) => ({ ...prev, [name]: value }))
  }

  const handleCampusChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target
    setCampusFormData((prev) => ({ ...prev, [name]: value }))
  }

  const handleSelectChange = (name: string, value: string) => {
    setCampusFormData((prev) => ({ ...prev, [name]: value }))
  }

  const nextStep = () => {
    setCompletedSteps((prev) => [...prev, currentStep])
    setCurrentStep((prev) => prev + 1)
  }

  const prevStep = () => {
    setCurrentStep((prev) => prev - 1)
  }

  const handleCreateSchool = async () => {
    setSubmitting(true)
    setError(null)

    try {
      // Create the school
      const schoolData = {
        name: schoolFormData.name,
        owner: 1, // This would normally come from the user's profile
      }

      const response = (await schoolAPI.create(schoolData)) as { id: number }
      setCreatedSchool(response)

      // Update campus form data with the school ID
      setCampusFormData((prev) => ({
        ...prev,
        school: response.id,
      }))

      // Move to the next step
      nextStep()
    } catch (err: any) {
      setError(err.message || "Failed to create school")
    } finally {
      setSubmitting(false)
    }
  }

  const handleCreateCampus = async () => {
    setSubmitting(true)
    setError(null)

    try {
      const response = await campusAPI.create(campusFormData)

      // Show success message
      setSuccess("Campus created successfully!")

      setTimeout(() => {
        router.push(`/dashboard`) // In a real app, this would be `/core/campuses/${response.id}/`
      }, 2000)
    } catch (err: any) {
      setError(err.message || "Failed to create campus")
    } finally {
      setSubmitting(false)
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    if (currentStep === 1) {
      await handleCreateSchool()
    } else if (currentStep === 5) {
      await handleCreateCampus()
    } else {
      nextStep()
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

  // Custom step indicator component
  const StepIndicator = ({ step, isActive, isCompleted }: { step: any; isActive: boolean; isCompleted: boolean }) => {
    const Icon = step.icon

    return (
      <div
        className={`flex items-center p-3 mb-2 rounded-lg transition-all duration-200 ${
          isActive
            ? "bg-primary/10 border-l-4 border-primary"
            : isCompleted
              ? "bg-green-50 border-l-4 border-green-500"
              : "hover:bg-gray-100"
        }`}
      >
        <div
          className={`flex items-center justify-center w-8 h-8 rounded-full mr-3 ${
            isActive ? "bg-primary text-white" : isCompleted ? "bg-green-500 text-white" : "bg-gray-200 text-gray-600"
          }`}
        >
          {isCompleted ? <CheckCircle2 className="h-5 w-5" /> : <Icon className="h-5 w-5" />}
        </div>
        <div>
          <p className={`font-medium ${isActive ? "text-primary" : ""}`}>{step.name}</p>
          <p className="text-xs text-gray-500">{step.description}</p>
        </div>
      </div>
    )
  }

  return (
    <div className="container mx-auto py-10 flex justify-center">
      <Card className="w-full max-w-5xl overflow-hidden shadow-lg border-0 bg-white">
        <div className="grid grid-cols-1 md:grid-cols-4">
          {/* Left sidebar with progress - now inside the card */}
          <div className="bg-gray-50 p-6 md:border-r border-gray-200">
            <h3 className="text-lg font-semibold mb-6 text-gray-800">Setup Progress</h3>
            <div className="space-y-1">
              {steps.map((step) => (
                <StepIndicator
                  key={step.id}
                  step={step}
                  isActive={currentStep === step.id}
                  isCompleted={completedSteps.includes(step.id)}
                />
              ))}
            </div>
          </div>

          {/* Right side with form - now inside the same card */}
          <div className="md:col-span-3 p-0">
            <CardHeader className="bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-gray-200">
              <CardTitle className="text-2xl text-gray-800">
                {steps.find((step) => step.id === currentStep)?.name}
              </CardTitle>
              <CardDescription className="text-gray-600">
                {steps.find((step) => step.id === currentStep)?.description}
              </CardDescription>
            </CardHeader>
            <CardContent className="p-6">
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
                <AnimatePresence mode="wait">
                  <motion.div
                    key={currentStep}
                    variants={formVariants}
                    initial="hidden"
                    animate="visible"
                    exit="exit"
                    className="max-w-md mx-auto"
                  >
                    {/* Step 1: School Information */}
                    {currentStep === 1 && (
                      <div className="space-y-4">
                        <div>
                          <Label htmlFor="name" className="text-gray-700">
                            School Name *
                          </Label>
                          <Input
                            id="name"
                            name="name"
                            value={schoolFormData.name}
                            onChange={handleSchoolChange}
                            required
                            placeholder="Enter school name"
                            className="mt-1"
                          />
                        </div>
                      </div>
                    )}

                    {/* Step 2: Campus Basic Info */}
                    {currentStep === 2 && (
                      <div className="space-y-4">
                        <div>
                          <Label htmlFor="campus-name" className="text-gray-700">
                            Campus Name *
                          </Label>
                          <Input
                            id="campus-name"
                            name="name"
                            value={campusFormData.name}
                            onChange={handleCampusChange}
                            required
                            placeholder="Enter campus name"
                            className="mt-1"
                          />
                        </div>

                        <div>
                          <Label htmlFor="code" className="text-gray-700">
                            Campus Code *
                          </Label>
                          <Input
                            id="code"
                            name="code"
                            value={campusFormData.code}
                            onChange={handleCampusChange}
                            required
                            placeholder="Enter campus code (e.g., MAIN)"
                            className="mt-1"
                          />
                        </div>

                        <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
                          <div>
                            <Label htmlFor="school_type" className="text-gray-700">
                              School Type *
                            </Label>
                            <Select
                              value={campusFormData.school_type}
                              onValueChange={(value) => handleSelectChange("school_type", value)}
                            >
                              <SelectTrigger className="mt-1 w-full">
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

                          <div>
                            <Label htmlFor="category" className="text-gray-700">
                              Category *
                            </Label>
                            <Select
                              value={campusFormData.category}
                              onValueChange={(value) => handleSelectChange("category", value)}
                            >
                              <SelectTrigger className="mt-1 w-full">
                                <SelectValue placeholder="Select category" />
                              </SelectTrigger>
                              <SelectContent>
                                <SelectItem value="mixed">Mixed</SelectItem>
                                <SelectItem value="boys">Boys Only</SelectItem>
                                <SelectItem value="girls">Girls Only</SelectItem>
                              </SelectContent>
                            </Select>
                          </div>
                        </div>
                      </div>
                    )}

                    {/* Step 3: Campus Contact Info */}
                    {currentStep === 3 && (
                      <div className="space-y-4">
                        <div>
                          <Label htmlFor="email" className="text-gray-700">
                            Campus Email *
                          </Label>
                          <Input
                            id="email"
                            name="email"
                            type="email"
                            value={campusFormData.email}
                            onChange={handleCampusChange}
                            required
                            placeholder="campus@example.com"
                            className="mt-1"
                          />
                        </div>

                        <div>
                          <Label htmlFor="phone" className="text-gray-700">
                            Campus Phone *
                          </Label>
                          <Input
                            id="phone"
                            name="phone"
                            value={campusFormData.phone}
                            onChange={handleCampusChange}
                            required
                            placeholder="+1234567890"
                            className="mt-1"
                          />
                        </div>

                        <div>
                          <Label htmlFor="website" className="text-gray-700">
                            Campus Website
                          </Label>
                          <Input
                            id="website"
                            name="website"
                            value={campusFormData.website}
                            onChange={handleCampusChange}
                            placeholder="https://www.yourcampus.com"
                            className="mt-1"
                          />
                        </div>
                      </div>
                    )}

                    {/* Step 4: Campus Location */}
                    {currentStep === 4 && (
                      <div className="space-y-4">
                        <div>
                          <Label htmlFor="address" className="text-gray-700">
                            Address *
                          </Label>
                          <Input
                            id="address"
                            name="address"
                            value={campusFormData.address}
                            onChange={handleCampusChange}
                            required
                            placeholder="123 Education Street"
                            className="mt-1"
                          />
                        </div>

                        <div className="grid grid-cols-1 gap-4 md:grid-cols-3">
                          <div>
                            <Label htmlFor="city" className="text-gray-700">
                              City *
                            </Label>
                            <Input
                              id="city"
                              name="city"
                              value={campusFormData.city}
                              onChange={handleCampusChange}
                              required
                              placeholder="City"
                              className="mt-1"
                            />
                          </div>

                          <div>
                            <Label htmlFor="state" className="text-gray-700">
                              State/Province *
                            </Label>
                            <Input
                              id="state"
                              name="state"
                              value={campusFormData.state}
                              onChange={handleCampusChange}
                              required
                              placeholder="State/Province"
                              className="mt-1"
                            />
                          </div>

                          <div>
                            <Label htmlFor="country" className="text-gray-700">
                              Country *
                            </Label>
                            <Input
                              id="country"
                              name="country"
                              value={campusFormData.country}
                              onChange={handleCampusChange}
                              required
                              placeholder="Country"
                              className="mt-1"
                            />
                          </div>
                        </div>
                      </div>
                    )}

                    {/* Step 5: Review & Submit */}
                    {currentStep === 5 && (
                      <div className="space-y-6">
                        <div className="rounded-lg border p-4 bg-blue-50">
                          <h3 className="font-medium mb-2 text-blue-800">School Information</h3>
                          <p>
                            <span className="text-gray-500">Name:</span>{" "}
                            <span className="font-medium">{schoolFormData.name}</span>
                          </p>
                        </div>

                        <div className="rounded-lg border p-4 bg-indigo-50">
                          <h3 className="font-medium mb-2 text-indigo-800">Campus Basic Information</h3>
                          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <p>
                              <span className="text-gray-500">Name:</span>{" "}
                              <span className="font-medium">{campusFormData.name}</span>
                            </p>
                            <p>
                              <span className="text-gray-500">Code:</span>{" "}
                              <span className="font-medium">{campusFormData.code}</span>
                            </p>
                            <p>
                              <span className="text-gray-500">Type:</span>{" "}
                              <span className="font-medium">{campusFormData.school_type}</span>
                            </p>
                            <p>
                              <span className="text-gray-500">Category:</span>{" "}
                              <span className="font-medium">{campusFormData.category}</span>
                            </p>
                          </div>
                        </div>

                        <div className="rounded-lg border p-4 bg-purple-50">
                          <h3 className="font-medium mb-2 text-purple-800">Campus Contact Information</h3>
                          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <p>
                              <span className="text-gray-500">Email:</span>{" "}
                              <span className="font-medium">{campusFormData.email}</span>
                            </p>
                            <p>
                              <span className="text-gray-500">Phone:</span>{" "}
                              <span className="font-medium">{campusFormData.phone}</span>
                            </p>
                            <p>
                              <span className="text-gray-500">Website:</span>{" "}
                              <span className="font-medium">{campusFormData.website || "N/A"}</span>
                            </p>
                          </div>
                        </div>

                        <div className="rounded-lg border p-4 bg-teal-50">
                          <h3 className="font-medium mb-2 text-teal-800">Campus Location</h3>
                          <p>
                            <span className="text-gray-500">Address:</span>{" "}
                            <span className="font-medium">{campusFormData.address}</span>
                          </p>
                          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-2">
                            <p>
                              <span className="text-gray-500">City:</span>{" "}
                              <span className="font-medium">{campusFormData.city}</span>
                            </p>
                            <p>
                              <span className="text-gray-500">State:</span>{" "}
                              <span className="font-medium">{campusFormData.state}</span>
                            </p>
                            <p>
                              <span className="text-gray-500">Country:</span>{" "}
                              <span className="font-medium">{campusFormData.country}</span>
                            </p>
                          </div>
                        </div>
                      </div>
                    )}
                  </motion.div>
                </AnimatePresence>
              </form>
            </CardContent>
            <CardFooter className="flex justify-center p-6 border-t border-gray-200 bg-gray-50 gap-4">
              <Button
                variant="outline"
                onClick={prevStep}
                disabled={currentStep === 1 || submitting}
                className="shadow-sm"
              >
                <ArrowLeft className="mr-2 h-4 w-4" />
                Back
              </Button>

              <Button
                onClick={handleSubmit}
                disabled={submitting}
                className="bg-gradient-to-r from-blue-600 to-indigo-600 shadow-md hover:shadow-lg transition-all"
              >
                {submitting ? (
                  <>
                    <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                    Processing...
                  </>
                ) : currentStep < 5 ? (
                  <>
                    Next
                    <ArrowRight className="ml-2 h-4 w-4" />
                  </>
                ) : (
                  "Create Campus"
                )}
              </Button>
            </CardFooter>
          </div>
        </div>
      </Card>
    </div>
  )
}
