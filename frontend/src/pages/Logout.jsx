import PageNavigation from "./PageNavigation";

export default function Logout() {
    return (
        <div>
             <PageNavigation />
            <h3>You sure you want to logout?</h3>
            <button>Back</button>
            <button>Confirm</button>
        </div>
    )
}


