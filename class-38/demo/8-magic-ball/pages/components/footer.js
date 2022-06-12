import Link from 'next/link'

export default function Footer({ latestAnswer }) {
  return (
    <footer className="flex justify-between bg-teal-600 py-4 items-center">
      <Link href={{ pathname: "components/result", query: { latestAnswer } }}>
        <a>result</a>
      </Link>
    </footer>
  );
}
