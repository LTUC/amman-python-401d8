
import Link from "next/link";
import { useRouter } from 'next/router';
export default function Result() {


    const router = useRouter();
    const data = router.query;

    return (
      <>
        <h1>{data.latestAnswer}</h1>
        <Link href={{ pathname: "/" }}>
          <a>back to Home</a>
        </Link>
      </>
    );
}