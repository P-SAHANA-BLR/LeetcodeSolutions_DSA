class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by '/' to isolate directory names and commands
        components = path.split('/')
        stack = []
        
        for component in components:
            # If the component is empty or '.', do nothing
            if component == "" or component == ".":
                continue
            # If '..', move up one directory level by popping from the stack
            elif component == "..":
                if stack:
                    stack.pop()
            # Otherwise, it's a valid directory name, add it to the stack
            else:
                stack.append(component)
                
        # Join the stack with '/' and prepend a leading '/'
        return "/" + "/".join(stack)
