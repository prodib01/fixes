import { Bell, ChevronDown, MoonIcon } from "lucide-react"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

export function Navbar() {
  return (
    <header className="border-b flex items-center justify-between px-6 py-3 bg-white">
      <div className="flex-1">
        <Select defaultValue="default">
          <SelectTrigger className="w-[180px]">
            <SelectValue placeholder="Select School" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="default">Main Campus</SelectItem>
            <SelectItem value="campus1">North Campus</SelectItem>
            <SelectItem value="campus2">South Campus</SelectItem>
          </SelectContent>
        </Select>
      </div>

      <div className="flex items-center gap-4">
        <Button variant="ghost" size="icon">
          <Bell className="h-5 w-5" />
        </Button>
        <Button variant="ghost" size="icon">
          <MoonIcon className="h-5 w-5" />
        </Button>
        <div className="flex items-center gap-2">
          <Avatar className="h-8 w-8 bg-gray-200">
            <AvatarFallback>A</AvatarFallback>
          </Avatar>
          <div className="flex flex-col text-xs">
            <span className="font-medium">admin</span>
            <span className="text-gray-500">Principal</span>
          </div>
          <ChevronDown className="h-4 w-4" />
        </div>
      </div>
    </header>
  )
}
